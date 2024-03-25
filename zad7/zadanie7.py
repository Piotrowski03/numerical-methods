import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])
B = np.array([[2],
              [6],
              [2]])


def metoda_gradientow_sprzezonych():
    rozmiar = (3,1)
    x = np.zeros(rozmiar)
    roznica = 1e-10
    r = B - np.dot(A, x)
    d = r

    while True:
        x0 = x.copy()
        a = np.dot(r.T, r) / np.dot(d.T, np.dot(A, d))
        x += a * d
        r0 = np.dot(r.T, r)
        r = B - np.dot(A, x)
        b = np.dot(r.T, r) / r0
        d = r + b*d
        norma = np.linalg.norm(r)
        if norma < 1:
            break

    return x


def main():
        wynik_gradientow_sprzezonych = metoda_gradientow_sprzezonych()
        print(wynik_gradientow_sprzezonych)


main()
