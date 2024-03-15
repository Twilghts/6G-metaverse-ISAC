import sympy

T = 2 * sympy.pi
M = 2 * sympy.pi / T
n = sympy.symbols('_n')
t = sympy.symbols('_t')
a = - T / 2
b = T / 2
ft = 2 * sympy.cos(2 * sympy.pi * t) - 3 * sympy.sin(4 * sympy.pi * t)
# Define your symbolic function
fn = (1 / T) * ft * sympy.exp(-sympy.I * n * M * t)

# Perform symbolic integration
Fn = sympy.integrate(fn, (t, a, b))


print("FN: ",  Fn)
