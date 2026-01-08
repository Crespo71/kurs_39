uczniowie = []
nauczyciele = []
wychowawca = []


def dodaj_ucznia():
    imie = input("Podaj imię i nazwisko ucznia: ")
    nazwa_klasy = input("Podaj nazwę klasy (np. 3C): ")
    uczniowie.append({"imie": imie, "klasa": nazwa_klasy})
    print("Dodano ucznia.\n")


def dodaj_nauczyciela():
    imie = input("Podaj imię i nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę przedmiotu: ")
    klasy = []
    print("Podawaj klasy prowadzone przez nauczyciela (pusta linia aby zakończyć):")
    while True:
        klasy_a = input()
        if klasy_a == "":
            break
        klasy.append(klasy_a)
    nauczyciele.append({"imie": imie, "przedmiot": przedmiot, "klasy": klasy})
    print("Dodano nauczyciela.\n")


def dodaj_wychowawca():
    imie = input("Podaj imię i nazwisko wychowawcy: ")
    nazwa_klasy_prowadzonej = input("Podaj nazwę prowadzonej klasy: ")
    wychowawca.append({"imie": imie, "klasa": nazwa_klasy_prowadzonej})
    print("Dodano wychowawcę.\n")


def zarzadzaj_klasa():
    numer_klasy = input("Podaj klasę do wyświetlenia: ")
    print(f"\nUczniowie klasy {numer_klasy}\n:")
    for uczen in uczniowie:
        if uczen["klasa"] == numer_klasy:
            print(" -", uczen["imie"])
    print("\nWychowawca:")
    for wychowawca1 in wychowawca:
        if wychowawca1["klasa"] == numer_klasy:
            print(" -", wychowawca1["imie"])
    print()


def zarzadzaj_uczen():
    imie = input("Podaj imię i nazwisko ucznia: ")
    klasa_ucznia = None
    for uczen in uczniowie:
        if uczen["imie"] == imie:
            klasa_ucznia = uczen["klasa"]
    if not klasa_ucznia:
        print("Nie znaleziono ucznia.\n")
        return
    print(f"\nLekcje ucznia {imie}:")
    for nauczyciel in nauczyciele:
        if klasa_ucznia in nauczyciel["klasa"]:
            print(f" - {nauczyciel['przedmiot']} (prowadzi: {nauczyciel['name']})")
    print()


def zarzadzaj_nauczyciel():
    imie = input("Podaj imię i nazwisko nauczyciela: ")
    for nauczyciel in nauczyciele:
        if nauczyciel["imie"] == imie:
            print(f"\nKlasy prowadzone przez {imie}:")
            for klasy in nauczyciele["klasa"]:
                print(" -", klasy)
            print()
            return
    print("Nie znaleziono nauczyciela.\n")


def zarzadzaj_wychowawca():
    imie = input("Podaj imię i nazwisko wychowawcy: ")
    klasa_nauczyciela = None
    for nauczyciel in klasa_nauczyciela:
        if nauczyciel["imie"] == imie:
            klasa_nauczyciela = nauczyciel["klasa"]
    if not klasa_nauczyciela:
        print("Nie znaleziono wychowawcy.\n")
        return
    print(f"\nUczniowie prowadzeni przez {imie}:")
    for uczen in uczniowie:
        if uczen["klasa"] == klasa_nauczyciela:
            print(" -", uczen["imie"])
    print()


def menu_tworzenia():
    while True:
        komenda = input("[Tworzenie] Wpisz: uczeń, nauczyciel, wychowawca, koniec: ")
        if komenda == "uczeń":
            dodaj_ucznia()
        elif komenda == "nauczyciel":
            dodaj_nauczyciela()
        elif komenda == "wychowawca":
            dodaj_wychowawca()
        elif komenda == "koniec":
            return
        else:
            print("Nieznana komenda.\n")


def menu_zarzadzania():
    while True:
        komenda = input("[Zarządzanie] Wpisz: klasa, uczeń, nauczyciel, wychowawca, koniec: ")
        if komenda == "klasa":
            zarzadzaj_klasa()
        elif komenda == "uczeń":
            zarzadzaj_uczen()
        elif komenda == "nauczyciel":
            zarzadzaj_nauczyciel()
        elif komenda == "wychowawca":
            zarzadzaj_wychowawca()
        elif komenda == "koniec":
            return
        else:
            print("Nieznana komenda.\n")


def polecenia() -> None:
    while True:
        komenda = input("Wpisz komendę: utwórz, zarządzaj, koniec: ")
        if komenda == "utwórz":
            menu_tworzenia()
        elif komenda == "zarządzaj":
            menu_zarzadzania()
        elif komenda == "koniec":
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieznana komenda.\n")


if __name__ == "__main__":

    polecenia()