import numpy as np
import matplotlib.pyplot as plt

# Función
def f(x):
    return x**2 + 3*x + 1

# Regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral, x, y

# Integral exacta
def exact_integral(a, b):
    return (b**3)/3 + (3*b**2)/2 + b - ((a**3)/3 + (3*a**2)/2 + a)

# Parámetros
a, b = 0, 2
n_values = [10, 20, 50]

# Valor exacto
I_exact = exact_integral(a, b)

print("Valor exacto de la integral:", round(I_exact, 6))

# ===== TABLA =====
print("\nTabla de resultados:")
print("{:<10} {:<25} {:<20}".format("n", "Integral aproximada", "Error"))

for n in n_values:
    I_approx, _, _ = trapezoidal_rule(a, b, n)
    error = abs(I_exact - I_approx)

    print("{:<10} {:<25.8f} {:<20.8f}".format(n, I_approx, error))

# ===== GRÁFICA =====
n_plot = 10
_, x_vals, y_vals = trapezoidal_rule(a, b, n_plot)

x_fine = np.linspace(a, b, 200)
y_fine = f(x_fine)

plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, label="f(x)=x^2+3x+1", linewidth=2)
plt.fill_between(x_vals, y_vals, alpha=0.3, label="Trapecios")
plt.plot(x_vals, y_vals, 'o-')

plt.title(f"Aproximación con regla del trapecio (n={n_plot})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.savefig("trapecio.png")
plt.show()
