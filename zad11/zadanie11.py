import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x, k):
    return k * x * (1 - x)

def generate_attractor(k, initial_condition, num_iterations):
    attractor = []

    xn = initial_condition
    for _ in range(num_iterations):
        xn = logistic_map(xn, k)
        attractor.append(xn)

    return attractor

def plot_attractor(k_values, initial_condition, num_iterations):
    for k in k_values:
        attractor = generate_attractor(k, initial_condition, num_iterations)
        plt.plot([k] * len(attractor), attractor, 'b.', markersize=0.5)

    plt.xlabel('Parameter 𝑘')
    plt.ylabel('Atraktor')
    plt.title('Atraktor dla odwzorowania logistycznego')
    plt.show()

# Przykładowe użycie
k_values = np.linspace(2, 4, 500)
initial_condition = 0.5
num_iterations = 100

plot_attractor(k_values, initial_condition, num_iterations)
