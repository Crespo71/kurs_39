# def witaj ():
#     print("=====Witaj w ma"gazynie wybierz funkcje=====\n")
from operator import truediv
historia = ["kupiono rolki", "sprzedano segway", "doładowano saldo o 10000"]
saldo = float(0)
magazyn = {
    "rower":             {"cena": 1200, "ilosc": 5},
    "hulajnoga":         {"cena": 350, "ilosc": 12},
    "deskorolka":        {"cena": 280, "ilosc":  7},
    "segway":            {"cena": 3200, "ilosc": 2},
    "rolki":             {"cena": 190, "ilosc": 18},
    "deskorolka_elekt.": {"cena": 1600, "ilosc": 3},
    "bmx":               {"cena": 1500, "ilosc": 4},
    "rower_elektryczny": {"cena": 5800, "ilosc": 1},
    "hulajnoga_elektr":  {"cena": 2100, "ilosc": 6},
    "monocykl":          {"cena": 2600, "ilosc": 2}
}


while True:
    start = int(input(f"===Witaj w programie===\n"
                      f"Wybierz co chcesz zrobić\n"
                      f"1.saldo\n"
                      f"2.sprzedaż\n"
                      f"3.zakup\n"
                      f"4.konto\n"
                      f"5.lista\n"
                      f"6.magazyn\n"
                      f"7.przeglad\n"
                      f"8.koniec\n"
                      f"\n"
                      f"Twój wybór: \n"))

    match start:
        case 1:
            saldo += float(input("Podaj kwotę doładowania: "))
            print(f"Saldo: {saldo}")
            input("Naciśnij 'enter' aby wrócić do menu")
            continue
        case 2:
            print("Jesteś w sprzedaży")
            produkt = input("Podaj nazwe produktu: ")
            if produkt in magazyn:
                obiekt = magazyn[produkt]
                cena = float(input("Podaj cenę: "))
                if cena == obiekt["cena"]:
                    ilosc = int(input("Podaj ilość: "))
                    if ilosc <= obiekt["ilosc"]:
                        obiekt["ilosc"] -= ilosc
                        saldo += cena*ilosc
                        print(f"Saldo: {saldo}")
                        print("Sprzedaż powiodła się!")
                    else:
                        print(f"Nie mamy tyle produktów typu {produkt} na stanie")
                else:
                    print(f"Podana cena nie zgadza sie z ceną {produkt}, która wynosi {obiekt["cena"]}")
            else:
                print(f"Nie mamy produktu {produkt} na stanie")
            continue
        case 3:
            print("Jestes w zakupie: ")
            produkt_nazwa = input("Podaj nazwę produktu, który chcesz dodać do magazynu: ")
            produkt_cena = float(input("Podaj cenę: "))
            produkt_ilosc = int(input("Podaj ilość: "))
            if produkt_cena <= 0:
                print("Cena nie może być mniejsza od zera")
            elif produkt_ilosc <= 0:
                print("Ilość nie może byc mniejsza od zera")
            elif produkt_ilosc*produkt_cena > saldo:
                print("Zbyt niskie saldo")
            else:
                if produkt_nazwa not in magazyn:
                    magazyn[produkt_nazwa] = {"cena": produkt_cena, "ilosc": produkt_ilosc}
                    saldo -= produkt_ilosc*produkt_cena
                    print(f"Stan salda: {saldo}")
                else:
                    istniejacy_produkt = magazyn[produkt_nazwa]
                    if istniejacy_produkt["cena"] == produkt_cena:
                        istniejacy_produkt["ilosc"] += produkt_ilosc
                        saldo -= produkt_ilosc*produkt_cena
                        print(f"Stan salda: {saldo}")
                    else:
                        print("Cena za towar nie zgadza się ze stanem")
            continue
        case 4:
            print("Jestes w koncie: ")
            print(f"Stan konta wynosi:  {saldo}")
            continue
        case 5:
            print("Jestes w liscie")
            print(f"Obecny stan magazynu to: {magazyn}")
            continue
        case 6:
            print("Jestes w magazynie: ")
            nazwa = input("Podaj nazwe produktu aby sprawdzić jego stan: ")
            if nazwa in magazyn:
                produkt = magazyn[nazwa]
                print(f"Produkt: {nazwa}")
                print(f"Ilość:   {produkt['ilosc']}")
                print(f"  Cena:  {produkt['cena']}")
                historia.append(produkt['cena'])
            else:
                print("Błąd: produkt nie znajduje się w magazynie.")
            continue
        case 7:
            od = input("Podaj zakres od: ")
            do = input("Podaj zakres do: ")
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do =len(historia)
            print(historia[od: do])
            continue
        case 8:
            print("Koniec progamu. Do widzenia")
            break
        case _:
            print("Wybierz opcje od 1 do 8")
            continue


