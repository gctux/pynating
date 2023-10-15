# Laufzeitvergleich Listen, arrange(), linspace()
import time as t
import numpy as np
# Python Liste
def version1(n):
    t1 = t.time()
    x1 = list(range(n)) # Liste erzeugen
    x2 = list(range(n))
    summe = []
    for i in range(n):
        summe.append(x1[i]+x2[i])
    return t.time() - t1

# NumPy arrange()
def version2(n):
    t1 = t.time()
    x1 = np.arange(n)
    x2 = np.arange(n)
    summe = x1 + x2
    return t.time() - t1

# NumPy linspace()
def version3(n):
    t1 = t.time()
    x1 = np.linspace(0,n,n)
    x2 = np.linspace(0,n,n)
    summe = x1 + x2
    return t.time() - t1

nt = 100000000

laufzeit1 = version1(nt)
laufzeit2 = version2(nt)
laufzeit3 = version3(nt)

faktor1 = laufzeit1/laufzeit2
faktor2 = laufzeit1/laufzeit3

print("Laufzeit für Python range()...:", laufzeit1)
print("Laufzeit für NumPy arange()...:", laufzeit2)
print("Laufzeit für NumPy linspace()...:", laufzeit3)
print("arrage() ist%4d mal schneller als range()" %faktor1)
print("linspace() ist%4d mal schneller als range()" %faktor2)