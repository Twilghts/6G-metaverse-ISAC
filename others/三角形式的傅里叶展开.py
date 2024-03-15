import sympy

T = 2 * sympy.pi
M = 2 * sympy.pi / T
n = sympy.symbols('_n')
t = sympy.symbols('_t')
a = - T / 2
b = T / 2
ft = t
# Define your symbolic function
fa0 = (1 / T) * ft
fan = (2 / T) * ft * sympy.cos(n * M * t)
fbn = (2 / T) * ft * sympy.sin(n * M * t)

# Perform symbolic integration
a0 = sympy.integrate(fa0, (t, a, b))
an = sympy.integrate(fan, (t, a, b))
bn = sympy.integrate(fbn, (t, a, b))

print("a0:", a0)
print("an:", an)
print("bn:", bn)
