import numpy as np
import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')
X = np.array([x, y, z])
A = np.array([1, 2, 3])
print(np.dot(X, A.T))
