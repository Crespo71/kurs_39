max_kg = 20
liczba_paczek = 0
waga_paczki = 0
kg_wyslanych = 0
najwiecej_pustych = 0
nr_paczki = 0

print("Ile elementów chcesz wysłać?")
ile = int(input())

licznik = 0

while licznik < ile:
    print("Podaj wagę elementu:")
    waga = float(input())

    if waga < 1 or waga > 10:
        print("Niepoprawna waga! Wysyłam.")
        break

    if waga_paczki + waga > max_kg:
        liczba_paczek = liczba_paczek + 1
        puste = max_kg - waga_paczki
        if puste > najwiecej_pustych:
            najwiecej_pustych = puste
            nr_paczki = liczba_paczek
        kg_wyslanych = kg_wyslanych + waga_paczki
        waga_paczki = 0

    waga_paczki = waga_paczki + waga
    licznik = licznik + 1

if waga_paczki > 0:
    liczba_paczek = liczba_paczek + 1
    puste = max_kg - waga_paczki
    if puste > najwiecej_pustych:
        najwiecej_pustych = puste
        nr_paczki = liczba_paczek
    kg_wyslanych = kg_wyslanych + waga_paczki

suma_pustych = liczba_paczek * max_kg - kg_wyslanych


print("Wysłano", liczba_paczek, "paczek")
print("Wysłano", kg_wyslanych, "kg towaru")
print("Suma pustych kilogramów:", suma_pustych, "kg")
print("Najwięcej pustych ma paczka", nr_paczki, "(", najwiecej_pustych, "kg )")