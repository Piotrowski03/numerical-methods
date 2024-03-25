import numpy as np
#determinanta tej macierzy to -x^3+12x^2-46x+56

def function(x):
    result = -x**3+12*x**2-46*x+56
    return result

def metoda_bisekcji(left_x,right_x):
    while (right_x - left_x) >= 1e-8:
        middle_x = (left_x + right_x) / 2

        if function(left_x) * function(middle_x) < 0:
            right_x = middle_x
        elif not function(left_x) * function(middle_x) > 0:
            return middle_x
        else:
            left_x = middle_x
    return right_x

def metoda_falsi(left_x,right_x):
    max_iter = 1000  # Maksymalna liczba iteracji (możesz dostosować według potrzeb)
    tol = 1e-9  # Tolerancja zbieżności

    for _ in range(max_iter):
        third = (function(left_x) * right_x - function(right_x) * left_x) / (function(left_x) - function(right_x))

        if abs(third - right_x) < tol:
            return third

        if function(left_x) * function(third) < 0:
            right_x = third
        elif function(right_x) * function(third) < 0:
            left_x = third

    return (right_x + left_x) / 2
def metoda_siecznych(x1, x2):
    max_iter = 1000  # Maksymalna liczba iteracji (możesz dostosować według potrzeb)
    tol = 1e-9  # Tolerancja zbieżności

    iter_count = 0

    while iter_count < max_iter:
        third = (function(x1) * x2 - function(x2) * x1) / (function(x1) - function(x2))

        if abs(function(third)) < tol:
            return third

        x1 = x2
        x2 = third
        iter_count += 1

def main():
    wynik_bisekcji1 = metoda_bisekcji(0, 3)
    wynik_bisekcji2 = metoda_bisekcji(3.1, 5)
    wynik_bisekcji3 = metoda_bisekcji(5.1, 7)

    wynik_falsi1 = metoda_falsi(0, 3)
    wynik_falsi2 = metoda_falsi(3.1, 5)
    wynik_falsi3 = metoda_falsi(5.1, 7)

    wynik_siecznych1 = metoda_siecznych(0, 3)
    wynik_siecznych2 = metoda_siecznych(3.1, 5)
    wynik_siecznych3 = metoda_siecznych(5.1, 7)

    print("Wyniki metody bisekcji :", wynik_bisekcji3, " ", wynik_bisekcji2, " ", wynik_bisekcji1)
    print("Wyniki metody falsi :", wynik_falsi3, " ", wynik_falsi2, " ", wynik_falsi1)
    print("Wyniki metody siecznych :", wynik_siecznych3, " ", wynik_siecznych2, " ", wynik_siecznych1)

main()

