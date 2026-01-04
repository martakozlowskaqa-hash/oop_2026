# zadanie

class FiguraGeometryczna:
    def __init__(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_pole(self):
        return a * b

    def policz_obwod(self):
        return 2 * (a + b)

figura1 = Prostokat(2,9)

# Pole_prostokata = a * b
# Obwod = a + b
print(Prostokat.policz_pole)
print(Prostokat.policz_obwod)

# Figura = input("Wpisz nazwe figury geometrycznej: ")
#
# class Kwadrat(Prostokat)
#     def __init__(self):
# #
# class Kolo(FiguraGeometryczna):
#     pass
#
# class Trojkat(FiguraGeometryczna):
#     pass
#
