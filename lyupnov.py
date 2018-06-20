import numpy as np
import matplotlib.pyplot as plt
from math import log
from math import exp
from decimal import Decimal
# show plots in notebook
# matplotlib inline

result = []
lambdas = []
maps = []

rvalues = np.arange(0, 3, 0.001)


for r in rvalues:
    x = 1.0
    result = []
    for t in range(0,1000):
        x = x**2*exp(r-x)
	if t > 800:
		maps.append(x) 
print len(maps)   

#fig = plt.figure(figsize=(10,7))
#ax1 = fig.add_subplot(1,1,1)

xticks = np.linspace(0, 3, 597000)
# zero line
#zero = [0]*4000
#ax1.plot(xticks, zero, 'g-')
# plot map
plt.plot(xticks, maps, 'b.',alpha = 0.3, label = 'Map')
plt.xlabel('A')
plt.ylabel('x')
plt.title(r"$Bifurcation\ for\ the\ map\ x_{n+1} = x_n^2e^{(A-x_n)}$")

# plot lyapunov
#ax1.plot(rvalues, lambdas, 'b-', linewidth = 3, label = 'Lyapunov exponent')
plt.grid('on')
#ax1.set_xlabel('r')
#ax1.legend(loc='best')
#ax1.set_title('Map of x(t+1) = x(t) + r - x(t)^2 versus Lyapunov exponent')
plt.show()

