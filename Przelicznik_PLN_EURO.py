# Program do przeliczenia waluty - PLN na EURO i EURO na PLN

class Zloty(float):
    def zamien_na_euro(self):
        return self / 4.21

class Euro(float):
    def zamien_na_pln(self):
        return self * 4.21

waluta = input("Wybierz walutę do przeliczenia (P - PLN na EUR, E - EUR na PLN): ").upper()

if waluta == "P":
    zl = input("Podaj wartosc w zlotowkach: ")
    try:
        zl = Zloty(zl)
        wynik = zl.zamien_na_euro()
        print(f"Wartosc w euro to: {wynik}")
    except ValueError:
        print("Podana wartosc nie jest liczba.")

elif waluta == "E":
    euro = input("Podaj wartosc w euro: ")
    try:
        euro = Euro(euro)
        wynik = euro.zamien_na_pln()
        print(f"Wartosc w zlotowkach to: {wynik}")
    except ValueError:
        print("Podana wartosc nie jest liczba.")

else:
    print("Niepoprawny wybor waluty.")