
MAX_WAGA_PACZKI = 20
MIN_WAGA = 1
MAX_WAGA = 10

ilosc = int(input("Ile elementów chcesz wysłać? "))

paczki = []         # lista z wagami paczek
waga_paczki = 0     # aktualna waga paczki

for i in range(1, ilosc + 1):
    waga = float(input(f"Podaj wagę elementu nr {i}: "))

    # sprawdzenie poprawności wagi
    if waga < MIN_WAGA or waga > MAX_WAGA:
        print("Niepoprawna waga – kończę przyjmowanie paczek.")
        break

    # jeśli element się nie mieści w paczce → zapisz paczkę i zacznij nową
    if waga_paczki + waga > MAX_WAGA_PACZKI:
        paczki.append(waga_paczki)
        waga_paczki = 0

    waga_paczki += waga

# dodaj ostatnią paczkę, jeśli nie jest pusta
if waga_paczki > 0:
    paczki.append(waga_paczki)

# --- PODSUMOWANIE ---
liczba_paczek = 0
kg_wyslanych = 0

for p in paczki:
    liczba_paczek = liczba_paczek + 1
    kg_wyslanych = kg_wyslanych + p

suma_pustych = liczba_paczek * MAX_WAGA_PACZKI - kg_wyslanych

# znajdź paczkę z największą ilością pustych kg
najwiecej_pustych = 0
nr_paczki = 0
numer = 0

for p in paczki:
    numer = numer + 1
    puste = MAX_WAGA_PACZKI - p
    if puste > najwiecej_pustych:
        najwiecej_pustych = puste
        nr_paczki = numer

print("Wysłano", liczba_paczek, "paczk" + ("ę" if liczba_paczek == 1 else "i"))
print("Wysłano", kg_wyslanych, "kg")
print("Suma pustych kilogramów:", int(suma_pustych), "kg")
print("Najwięcej pustych kilogramów ma paczka", nr_paczki, f"({int(najwiecej_pustych)} kg)")