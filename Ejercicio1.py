import numpy as np
import matplotlib.pyplot as plt

# Función del ejercicio
def f(x):
    return np.sin(x)

# Derivada analítica
def df_exact(x):
    return np.cos(x)

# Métodos de diferencias finitas
def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# Parámetros
h = 0.1
x_vals = np.arange(0, np.pi + h, h)

# Evaluaciones
f_vals = f(x_vals)
df_vals = df_exact(x_vals)

# Aproximaciones
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Errores
error_forward = np.abs(df_forward - df_vals)
error_backward = np.abs(df_backward - df_vals)
error_central = np.abs(df_central - df_vals)

# -------- TABLA EN CONSOLA --------
print("x\t f(x)\t Derivada\t Adelante\t Atrás\t Centrada\t Err_Adel\t Err_Atrás\t Err_Cent")
for i in range(len(x_vals)):
    print(f"{x_vals[i]:.2f}\t {f_vals[i]:.4f}\t {df_vals[i]:.4f}\t {df_forward[i]:.4f}\t {df_backward[i]:.4f}\t {df_central[i]:.4f}\t {error_forward[i]:.4f}\t {error_backward[i]:.4f}\t {error_central[i]:.4f}")

# -------- GRÁFICA 1 --------
plt.figure()
plt.plot(x_vals, f_vals, label='f(x)=sin(x)')
plt.plot(x_vals, df_vals, label='Derivada exacta cos(x)')
plt.plot(x_vals, df_forward, '--', label='Adelante')
plt.plot(x_vals, df_backward, '-.', label='Atrás')
plt.plot(x_vals, df_central, ':', label='Centrada')
plt.xlabel('x')
plt.ylabel('Valores')
plt.title('Comparación de Derivadas')
plt.legend()
plt.grid()
plt.show()

# -------- GRÁFICA 2 --------
plt.figure()
plt.plot(x_vals, error_forward, '--', label='Error Adelante')
plt.plot(x_vals, error_backward, '-.', label='Error Atrás')
plt.plot(x_vals, error_central, ':', label='Error Centrada')
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.title('Errores de los Métodos')
plt.legend()
plt.grid()
plt.show()