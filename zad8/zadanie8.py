import numpy as np
import sys
# Macierz A z treści zadania
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, -1]])

# Rozmiar macierzy
n = A.shape[0]

# Metoda potęgowa

def power_method(matrix, epsilon=1e-8, max_iterations=1000):
    n = matrix.shape[0]
    matrix = matrix.astype(float)  # Convert matrix to float type
    eigenvalues = []
    eigenvectors = []

    for i in range(n):
        x = np.ones(n)  # Initial vector
        eigenvalue_prev = 0

        for iteration in range(max_iterations):
            y = np.dot(matrix, x)
            eigenvalue = np.dot(x, y)

            # Normalization
            x = y / np.linalg.norm(y)

            # Check convergence condition
            if np.abs(eigenvalue - eigenvalue_prev) < epsilon:
                break

            eigenvalue_prev = eigenvalue

        eigenvalues.append(eigenvalue)
        eigenvectors.append(x)

        # Deflation: removing the eigenvalue component from the matrix
        matrix -= eigenvalue * np.outer(x, x)

    return eigenvalues, eigenvectors

# Metoda Rayleigha
def rayleigh_quotient(matrix, x):
    return np.dot(x, np.dot(matrix, x)) / np.dot(x, x)

def rayleigh_method(matrix, epsilon=1e-8, max_iterations=1000):
    x = np.ones(n)  # Początkowy wektor
    eigenvalue_prev = 0

    for iteration in range(max_iterations):
        mu = rayleigh_quotient(matrix, x)

        # Rozwiązanie układu równań (A - mu*I)y = x
        y = np.linalg.solve(matrix - mu * np.eye(n), x)

        # Normalizacja
        x = y / np.linalg.norm(y)

        # Sprawdzenie warunku zbieżności
        if np.linalg.norm(y) < epsilon:
            break

        eigenvalue_prev = mu

    return mu, x


# Metoda iteracyjna QR
def qr_iteration(matrix, epsilon=1e-8, max_iterations=1000):
    B = np.copy(matrix)
    eigenvalues = []

    for iteration in range(max_iterations):
        Q, R = np.linalg.qr(B)
        B = np.dot(R, Q)

        eigenvalues.append(B.diagonal())

        # Sprawdzenie warunku zbieżności
        if np.linalg.norm(np.tril(B, k=-1)) < epsilon:
            break

    return eigenvalues[-1], Q[:, 0]

# Znalezienie wartości własnych przy użyciu wszystkich trzech metod
eigenvalue_power, eigenvector_power = power_method(A)
eigenvalue_rayleigh, eigenvector_rayleigh = rayleigh_method(A)
eigenvalue_qr, eigenvector_qr = qr_iteration(A)

# Wyświetlenie wyników
print("Metoda potęgowa:")
print("Wartości własne:", eigenvalue_power)


print("\nMetoda Rayleigha:")
print("Wartości własne:", eigenvalue_rayleigh)


print("\nMetoda iteracyjna QR:")
print("Wartości własne:", eigenvalue_qr)
