from sympy import *
x = symbols("x")
y = x**3-7*x**2+7*x+15
y_1 = diff(y, x, 1)
y_2 = diff(y, x, 2)
y_3 = diff(y, x, 3)
Y = integrate(y,x)
print("1. Ableitung", y_1)
print("2. Ableitung", y_2)
print("3. Ableitung", y_3)
print("Stammfunktion", Y)