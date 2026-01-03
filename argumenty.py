# Przekazywanie argumentow do funkcji
# Argumenty pozycyjne
def dodaj(a, b):
    return a+b
dodaj(6, 7)
# wiele argumentow - krotka *args - moge podawac wiele argumentow
def dodaj2(*args):
    #zmienna lokalna
    wynik = 0
    for arg in args:
        wynik += arg
    return wynik

print(dodaj2(2, 4, 5, 6, 8))
# wiele argumentow - krotka *args - moge podawac wiele argumentow + jeden paramter slownikowy
def dodaj3(*args, verbose=False):
    if verbose == True:
        print(f"Wykonam dzialanie. Dodam {args}")
    wynik = 0
    for arg in args:
        wynik += arg
    return wynik

print(dodaj3(3, 6 , 7))
print(dodaj3(5, 6, 7 , 7, verbose=True))

# wiele argumentow - krotka *args - moge podawac wiele argumentow + **kwargs - wiele argumentow slownikowych
def dodaj4(*args, **kwargs):
    if kwargs['verbose'] == True:
        print("Wykonam dzialanie.")
    wynik = 0

    for arg in args:
        wynik -= arg
    return wynik

print(dodaj4(1, 2, 3, 6, verbose=True, parametr="wartosc"))