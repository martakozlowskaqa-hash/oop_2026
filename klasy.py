# Klasa = Szablon, Przepis


class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self):
    # Konstruktor
    # Akt istnienia
        print("Niech powstanie czlowiek")
    pass

# Powstawanie obiektu , gotowanie z przepisu
adam = Czlowiek()
# print(type(adam))
# print(dir(adam))
print(adam.gatunek)