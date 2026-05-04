import numpy as np
import matplotlib.pyplot as plt

# Función del ejercicio
def f(x):
    return np.exp(-x**2)

# Regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral

# Intervalo
a, b = 1, 4

# Valores de n del ejercicio
n_values = [5, 10, 15]

# Valor de referencia (usando n muy grande)
n_ref = 100000
I_exact = trapezoidal_rule(a, b, n_ref)

print("Valor de referencia (aproximado):", round(I_exact, 8))
print("\nResultados:\n")

errors = []

for n in n_values:
    I_approx = trapezoidal_rule(a, b, n)
    error = abs(I_exact - I_approx)
    errors.append(error)

    print(f"n = {n}")
    print(f"Integral aproximada = {I_approx:.8f}")
    print(f"Error = {error:.8f}")
    print("-" * 30)

# Gráfica de convergencia
plt.figure(figsize=(8, 5))
plt.plot(n_values, errors, marker='o')
plt.title("Convergencia de la regla del trapecio")
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error")
plt.grid()

plt.savefig("convergencia_trapecio.png")
plt.show()
