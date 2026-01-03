# Klasa = Szablon, Przepis

class Czlowiek:
    # ten gatunek to atrybut klasy
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec): # atrybuty obiektu (skladniki), jesli podajemy atrybut musimy go okreslic nie mozna zostawic nieokreslonej.
    #     obejscie tego bledu to bedzie atrybut imie=None lub imie="Bezimmieny" - wtedy nie bedzie bledu to bedzie domyslna wartosc
    # Konstruktor
    # Akt istnienia
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec

    # metoda, mozliwosc moznosc, zdolnosc
    def przedstaw_sie(self):

        print(f"Mam na imie {self.imie}. Jestem ", end="")
        if self.plec=="M":
            print("mezczyzna")
        else:
            print("kobieta")
        # lub print(f"Mam na imie {self.imie}. Jestem {self.plec}")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")


class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa!")

    def przedstaw_sie(self):

        print(f"hejcia jestem {self.imie}. Ja to ", end="")
        if self.plec == "M":
            print("chlopiec")
        else:
            print("dziewczynka")

# Powstawanie obiektu , gotowanie z przepisu
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")
# print(adam.gatunek)
# print(ewa.gatunek)
# print(adam.imie)
# print(ewa.imie)

ewa.przedstaw_sie()
ewa.przedstaw(adam)

kain = Dziecko("Kain", "M")
kain.baw_sie()
kain.przedstaw_sie()