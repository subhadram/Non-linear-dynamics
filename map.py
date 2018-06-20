import numpy as np
import matplotlib.pyplot as plt
a = 1.0
def mp(x):
	y = a*x*(1-x)
	return y
x = np.arange(0,10)
y = mp(x)
z = mp(y)



plt.plot(x,y)
plt.plot(x,z)
plt.show()

