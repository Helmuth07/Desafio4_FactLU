import numpy as np
from scipy.linalg import lu

# Definimos la matriz A y el vector B
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]])

B = np.array([27, -61.5, -21.5])

# Realizamos la descomposición LU
P, L, U = lu(A)

# Mostrar las matrices L y U
print("Matriz L:")
print(L)

print("\nMatriz U:")
print(U)

# Resolver el sistema L * y = B
y = np.linalg.solve(L, B)

# Resolver el sistema U * x = y
x = np.linalg.solve(U, y)

print("\nSolución del sistema:")
print(x)
