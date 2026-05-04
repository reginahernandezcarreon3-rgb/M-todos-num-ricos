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
C = 1e-6
a = 0
b = 5

# Función V(t)
def V(t):
    return 100 * np.exp(-2*t)

# Solución analítica
exacta = C * (100/2) * (1 - np.exp(-2*b))  # integral de e^{-2t}
print(f"Solución exacta: {exacta:.10f}")

# Valores de n
valores_n = [6, 10, 20, 30]

errores = []
resultados = []

for n in valores_n:
    aprox = C * simpson_rule(V, a, b, n)
    error = abs(exacta - aprox)
    
    resultados.append(aprox)
    errores.append(error)
    
    print(f"n = {n} -> Aproximación: {aprox:.10f}, Error: {error:.2e}")

# Gráfica de la función
t_vals = np.linspace(a, b, 100)
v_vals = V(t_vals)

plt.figure()
plt.plot(t_vals, v_vals, label="V(t) = 100e^{-2t}")
plt.fill_between(t_vals, v_vals, alpha=0.3, label="Área")
plt.title("Voltaje en el capacitor")
plt.xlabel("t")
plt.ylabel("V(t)")
plt.legend()
plt.grid()
plt.savefig("capacitor.png")
plt.show()

# Gráfica del error
plt.figure()
plt.plot(valores_n, errores, marker='o')
plt.title("Error vs número de subintervalos")
plt.xlabel("n")
plt.ylabel("Error")
plt.grid()
plt.savefig("error_capacitor.png")
plt.show()
