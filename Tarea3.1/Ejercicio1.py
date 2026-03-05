import numpy as np
import matplotlib.pyplot as plt

def gauss_elimination_with_errors(A, b):
    n = len(b)
    A = A.copy()
    b = b.copy()
    errors = []

    for i in range(n):
        # Pivoteo parcial
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        # Eliminación hacia adelante
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
        
        # Guardar error de residuo en cada paso
        x_partial = np.zeros(n)
        for k in range(i+1):
            x_partial[k] = b[k] / A[k, k]
        residual = np.linalg.norm(np.dot(A, x_partial) - b)
        errors.append(residual)
    
    # Sustitución regresiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x, errors

# Definición del sistema
A = np.array([[3, 2, -1, 4], [5, -3, 2, -1], [-1, 4, -2, 3], [2, -1, 3, 5]], dtype=float)
b = np.array([10, 5, -3, 8], dtype=float)

# Resolución con errores
sol, errors = gauss_elimination_with_errors(A, b)

print("Solución del sistema:")
print(sol)

# Gráfica de errores
plt.plot(range(1, len(errors)+1), errors, marker='o')
plt.xlabel("Paso de eliminación")
plt.ylabel("Error del residuo ||Ax - b||")
plt.title("Convergencia de la eliminación gaussiana")
plt.grid(True)
plt.show()
