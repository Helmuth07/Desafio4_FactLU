import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la matriz A y el vector B
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]])

B = np.array([27, -61.5, -21.5])

# Crear la figura para el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear una cuadrícula de puntos en el espacio (x2, x3)
x2, x3 = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))

# Definir los tres planos usando las ecuaciones Ax = B
# Ecuaciones:  A[0,0]*x1 + A[0,1]*x2 + A[0,2]*x3 = B[0]
x1_1 = (B[0] - A[0,1]*x2 - A[0,2]*x3) / A[0,0]
x1_2 = (B[1] - A[1,1]*x2 - A[1,2]*x3) / A[1,0]
x1_3 = (B[2] - A[2,1]*x2 - A[2,2]*x3) / A[2,0]

# Graficar los tres planos
ax.plot_surface(x2, x3, x1_1, alpha=0.5, rstride=100, cstride=100, color='blue')
ax.plot_surface(x2, x3, x1_2, alpha=0.5, rstride=100, cstride=100, color='green')
ax.plot_surface(x2, x3, x1_3, alpha=0.5, rstride=100, cstride=100, color='red')

# Solución del sistema
x_sol = np.linalg.solve(A, B)

# Graficar la solución como un punto
ax.scatter(x_sol[1], x_sol[2], x_sol[0], color='black', s=100, label="Solución (0.5, 8, -6)")

# Etiquetas y límites de los ejes
ax.set_xlabel('x2')
ax.set_ylabel('x3')
ax.set_zlabel('x1')

plt.title('Intersección de los tres planos (solución)')
plt.legend()
plt.show()
