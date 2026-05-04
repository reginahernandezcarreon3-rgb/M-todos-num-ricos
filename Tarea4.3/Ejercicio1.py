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

# Parámetros del problema
k = 200
a = 0.1
b = 0.3

# Función del resorte
def funcion(x):
    return k * x

# Solución analítica
exacta = (k / 2) * (b**2 - a**2)
print(f"Solución exacta: {exacta}")

# Valores de n
valores_n = [6, 10, 20, 30]

errores = []
resultados = []

for n in valores_n:
    aprox = simpson_rule(funcion, a, b, n)
    error = abs(exacta - aprox)
    
    resultados.append(aprox)
    errores.append(error)
    
    print(f"n = {n} -> Aproximación: {aprox:.6f}, Error: {error:.6e}")

# Gráfica de la función
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

plt.figure()
plt.plot(x_vals, y_vals, label="f(x) = kx")
plt.fill_between(x_vals, y_vals, alpha=0.3, label="Área (trabajo)")
plt.scatter(np.linspace(a, b, 10), funcion(np.linspace(a, b, 10)), label="Puntos")
plt.title("Trabajo de un resorte")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.legend()
plt.grid()
plt.savefig("resorte.png")
plt.show()

# Gráfica del error
plt.figure()
plt.plot(valores_n, errores, marker='o')
plt.title("Error vs número de subintervalos")
plt.xlabel("n")
plt.ylabel("Error")
plt.grid()
plt.savefig("error.png")
plt.show()
