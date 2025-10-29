# dane zadania
imie_odbiorcy = input("Podaj imię solenizanta: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiadomosc = ("Wszystkiego najlepszego z okazji urodzin.")
imie_nadawcy = input("Podaj swoje imię: ")

# wieku odbiorcy
from datetime import date
obecny_rok = date.today().year
wiek = obecny_rok - rok_urodzenia  #lub wiek = 2025 - rok_urodzenia
#wiek = 2025 - rok_urodzenia

# Wygenerowanie kartki

print(f"Kartka Urodzinowa dla {imie_odbiorcy}")
print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!\n")
print(f"Z serdecznymi życzeniami,{imie_nadawcy}")