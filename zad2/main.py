import matplotlib.pyplot as plt
import numpy as np
import math

def function(x):
    return np.sin(x)
def pochodna(x):
    return np.cos(x)

def pochodna_a(h, x):
    return (function(x + h) - function(x)) / h

def pochodna_b(h, x):
    return (function(x + h) - function(x - h)) / (2 * h)

def pochodna_c(h, x):
    return (-1 * function(x + 2 * h) + 8 * function(x + h) - 8 * function(x - h) + function(x - 2 * h)) / (12 * h)
def errorvalue(x, h, pochodna_):
    exact_value = pochodna(x)
    somewhat_value = pochodna_(h, x)
    error = abs(exact_value - somewhat_value)
    return error

x_values = 1  # x = π/2
h_values = np.logspace(-16, 0, 100)  # Range of h values on a logarithmic scale

errors_a = [errorvalue(x_values, h, pochodna_a) for h in h_values]
errors_b = [errorvalue(x_values, h, pochodna_b) for h in h_values]
errors_c = [errorvalue(x_values, h, pochodna_c) for h in h_values]

    # Plot the results on a logarithmic scale
plt.loglog(h_values, errors_a, label='Method 2a')
plt.loglog(h_values, errors_b, label='Method 2b')
plt.loglog(h_values, errors_c, label='Method 2c')

plt.xlabel('h')
plt.ylabel('|Dh f(x) - f\'(x)|')
plt.legend()
plt.title("błąd dyskretyzacji dla x=1")
plt.show()
x_values = np.pi / 2  # x = π/2
h_values = np.logspace(-16, 0, 100)  # Range of h values on a logarithmic scale

errors_a = [errorvalue(x_values, h, pochodna_a) for h in h_values]
errors_b = [errorvalue(x_values, h, pochodna_b) for h in h_values]
errors_c = [errorvalue(x_values, h, pochodna_c) for h in h_values]

    # Plot the results on a logarithmic scale
plt.loglog(h_values, errors_a, label='Method 2a')
plt.loglog(h_values, errors_b, label='Method 2b')
plt.loglog(h_values, errors_c, label='Method 2c')

plt.xlabel('h')
plt.ylabel('|Dh f(x) - f\'(x)|')
plt.legend()
plt.title("błąd dyskretyzacji dla x = pi/2")
plt.show()

