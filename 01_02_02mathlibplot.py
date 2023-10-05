import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,6,0.01)
y = x**3-7*x**2+7*x+15
plt.plot(x,y)
plt.show()
