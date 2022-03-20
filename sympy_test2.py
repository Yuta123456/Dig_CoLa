import numpy as np
import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
exp = (x + y) ** 2
exp = sympy.expand(exp)
print(exp)
print(exp.coeff(x * y, 1))
