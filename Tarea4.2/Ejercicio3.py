import numpy as np
import matplotlib.pyplot as plt

# Función
def f(x):
    return np.sin(x)

# Regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral, x, y

# Intervalo
a, b = 0, np.pi

# Valores de n
n_values = [5, 10, 20, 50]

# Valor exacto
I_exact = 2

print("Valor exacto:", I_exact)
print("\nResultados:\n")

for n in n_values:
    I_approx, _, _ = trapezoidal_rule(a, b, n)
    error = abs(I_exact - I_approx)

    print(f"n = {n}")
    print(f"Integral aproximada = {I_approx:.8f}")
    print(f"Error = {error:.8f}")
    print("-" * 30)

# ====== GRÁFICA ======
x_fine = np.linspace(a, b, 200)
y_fine = f(x_fine)

plt.figure(figsize=(8,5))
plt.plot(x_fine, y_fine, label="f(x)=sin(x)", linewidth=2)

# Dibujar trapecios para n=10 (ejemplo visual)
n_plot = 10
_, x_vals, y_vals = trapezoidal_rule(a, b, n_plot)

plt.fill_between(x_vals, y_vals, alpha=0.3, label="Trapecios (n=10)")
plt.plot(x_vals, y_vals, 'o-')

plt.title("Aproximación de ∫ sin(x) dx con regla del trapecio")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.savefig("trapecio_sin.png")
plt.show()
