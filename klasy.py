# Klasa = Szablon, Przepis


class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
    # Konstruktor
    # Akt istnienia
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie

# Powstawanie obiektu , gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
# print(type(adam))
# print(dir(adam))
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)