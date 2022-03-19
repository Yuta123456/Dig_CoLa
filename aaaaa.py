import numpy as np
import sympy

x = np.array([sympy.Symbol('x1'), sympy.Symbol('x2'),sympy.Symbol('x3')])

q = np.array([[2, 0, -1],
              [0, 0.2, 0],
              [-1, 0, 2]])
c = np.array([0,-1,0]).T

A = [1,1,1]
ans = (1/2) * np.dot(np.dot(x.T, q), x) + np.dot(c.T, x)
print(sympy.expand(ans))