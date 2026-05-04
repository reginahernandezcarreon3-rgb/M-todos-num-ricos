import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Parámetros
k = 0.5
a = 0
b = 2

# Derivada de la temperatura
def dTdx(x):
    return -100 * x

# Solución exacta
exacta = k * (-50 * b**2)
print(f"Solución exacta: {exacta}")

# Valores de n
valores_n = [6, 10, 20, 30]

errores = []

for n in valores_n:
    aprox = k * simpson_rule(dTdx, a, b, n)
    error = abs(exacta - aprox)
    
    print(f"n = {n} -> Aproximación: {aprox:.6f}, Error: {error:.2e}")
    errores.append(error)

# Gráfica de dT/dx
x_vals = np.linspace(a, b, 100)
y_vals = dTdx(x_vals)

plt.figure()
plt.plot(x_vals, y_vals, label="dT/dx = -100x")
plt.fill_between(x_vals, y_vals, alpha=0.3, label="Área")
plt.title("Flujo de calor")
plt.xlabel("x")
plt.ylabel("dT/dx")
plt.legend()
plt.grid()
plt.savefig("calor.png")
plt.show()

# Gráfica del error
plt.figure()
plt.plot(valores_n, errores, marker='o')
plt.title("Error vs n")
plt.xlabel("n")
plt.ylabel("Error")
plt.grid()
plt.savefig("error_calor.png")
plt.show()
