class FiguryGeometryczne:
    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

class Prostokat(FiguryGeometryczne):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def policz_pole(self):
        return self.a * self.b

    def policz_obwod(self):
        return 2 * (self.a + self.b)

prostokat = Prostokat(7,3)

print(prostokat.policz_obwod())
print(prostokat.policz_pole())

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)
        # Prostokat(a, a)

kwadrat = Kwadrat(3)

print(kwadrat.policz_pole())

class Kolo(FiguryGeometryczne):
    def __init__(self, r):
        self.r = r
    def policz_pole(self):
        return 3.14 * (self.r * self.r)

    def policz_obwod(self):
        return 2 * (self.r * 3.14)

kolo = Kolo(4)

print(kolo.policz_pole())
print(kolo.policz_obwod())

class Trojkat(FiguryGeometryczne):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        (a * h) / 2
    def policz_pole(self):
        return (self.a * self.h) / 2

    def policz_obwod(self):
        return self.a + self.b + self.c

trojkat = Trojkat(2,4,4,6)

print(trojkat.policz_obwod())
print(trojkat.policz_pole())