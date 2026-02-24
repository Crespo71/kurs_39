import json
import os
import requests
from datetime import datetime, timedelta


class WeatherForecast:
    def __init__(self, filename="weather_cache.json", latitude=57.1167, longitude=-17.0333):

        self.filename = filename
        self.latitude = latitude
        self.longitude = longitude
        self._data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self._data = json.load(f)

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4)


    def _fetch_from_api(self, date):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            "&hourly=rain"
            "&daily=rain_sum"
            "&timezone=Europe%2FLondon"
            f"&start_date={date}"
            f"&end_date={date}"
        )

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            rain_sum = data.get("daily", {}).get("rain_sum", [None])[0]

            if rain_sum is None or rain_sum < 0:
                return "Nie wiem"
            elif rain_sum == 0.0:
                return "Nie będzie padać"
            else:
                return "Będzie padać"

        except Exception:
            return "Nie wiem"


    def __getitem__(self, date):
        if date not in self._data:
            result = self._fetch_from_api(date)
            self._data[date] = result
            self._save()
        return self._data[date]

    def __setitem__(self, date, value):
        self._data[date] = value
        self._save()

    def __iter__(self):
        return iter(self._data)

    def items(self):
        for key, value in self._data.items():
            yield key, value


def main():
    wf = WeatherForecast()

    user_input = input("Podaj datę (YYYY-mm-dd) lub naciśnij Enter: ").strip()

    if not user_input:
        searched_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            searched_date = user_input
        except ValueError:
            print("zły format daty.")
            return

    result = wf[searched_date]
    print(f"\nPrognoza na {searched_date}: {result}")


if __name__ == "__main__":
    main()