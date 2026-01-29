import requests
import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "zajecia_15/weather_cache.json"

LATITUDE = 57.1167    # Wrocław
LONGITUDE = 17.0333   # Wrocław

def get_next_day():
    return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4, ensure_ascii=False)

def check_rain_from_api(date_str):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}"
        f"&longitude={LONGITUDE}"
        f"&hourly=rain"
        f"&daily=rain_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date_str}"
        f"&end_date={date_str}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        rain_sum = data.get("daily", {}).get("rain_sum", [])

        if not rain_sum or rain_sum[0] is None:
            return "Nie wiem"

        value = rain_sum[0]

        if value < 0:
            return "Nie wiem"
        elif value == 0.0:
            return "Nie będzie padać"
        elif value > 0.0:
            return "Będzie padać"
        else:
            return "Nie wiem"

    except Exception:
        return "Nie wiem"


def main():
    user_date = input("Podaj datę (YYYY-mm-dd) lub naciśnij [Enter = jutro]: ").strip()

    if not user_date:
        searched_date = get_next_day()
    else:
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
            searched_date = user_date
        except ValueError:
            print("❌ Niepoprawny format daty. Użyj YYYY-mm-dd")
            return

    cache = load_cache()

    if searched_date in cache:
        result = cache[searched_date]
        print(f"(z pliku) {searched_date} → {result}")
        return

    result = check_rain_from_api(searched_date)

    cache[searched_date] = result
    save_cache(cache)

    print(f"(z API) {searched_date} → {result}")

if __name__ == "__main__":
    main()