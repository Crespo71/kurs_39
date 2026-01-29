import requests
import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "pogoda_cache.json"

Szerokosc= 57.1167
Dlugosc = 17.0333


def jutro_opad():
    return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")


def wczytaj_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def zapisz_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4, ensure_ascii=False)


def opad_z_api(date_str):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={Szerokosc}"
        f"&longitude={Dlugosc}"
        f"&hourly=rain"
        f"&daily=rain_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date_str}"
        f"&end_date={date_str}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()


        suma_opadow = data.get("daily", {}).get("suma_opadow", [])

        if not suma_opadow or suma_opadow[0] is None:
            return "Nie wiem"

        wartosc = suma_opadow[0]

        if wartosc < 0:
            return "Nie wiem"
        elif wartosc == 0.0:
            return "Nie będzie padać"
        elif wartosc > 0.0:
            return "Będzie padać"
        else:
            return "Nie wiem"

    except Exception:
        return "Nie wiem"

def main():
    data_uzytkownika = input("Podaj datę (YYYY-mm-dd), [Enter = jutro]: ").strip()

    if not data_uzytkownika:
        szukana_data = jutro_opad()
    else:

        try:
            datetime.strptime(data_uzytkownika, "%Y-%m-%d")
            szukana_data = data_uzytkownika
        except ValueError:
            print("❌ Zły format daty, Użyj YYYY-mm-dd")
            return

    cache = wczytaj_cache()

    if szukana_data in cache:
        result = cache[szukana_data]
        print(f"(z pliku) {szukana_data} → {result}")
        return

    result = opad_z_api(szukana_data)

    cache[szukana_data] = result
    zapisz_cache(cache)

    print(f"(z API) {szukana_data} → {result}")

if __name__ == "__main__":
    main()
