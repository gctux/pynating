import numpy as np
# 03_01_02_zweidim_array.py

m = 3 #Zeilen
n = 4 #Spalten
a = np.arange(m*n).reshape(m,n)
b = a.reshape(n*m,)
print("Typ des Arrays",a.shape,"\n",a)
print("Linearisieren\n",b)
print("Transponieren\n",a.T)
