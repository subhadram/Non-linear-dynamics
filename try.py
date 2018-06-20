import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

b = np.arange(0,1.3,0.01)
mx = np.zeros(len(b))
mn = np.zeros(len(b))
I= 1
a = 1

def myModel(y, t, f):
    dy0 = y[1] + y[0] - y[0]**3/3 + I
    dy1 = y[0] + a - f*y[1]
    return [dy0, dy1]

i = 0
for f in b:
    time = np.arange(0.0, 2000,0.01)
    yinit = np.array([0.1, 0.1])
    y = odeint(myModel, yinit, time, args=(f,))
    plt.plot(y[:,0],y[:,1])
    mx[i] = np.max(y[-600:-1,0])
    mn[i] = np.min(y[-600:-1,0])
    i += 1


#plt.plot(b,mx)
#plt.plot(b,mn)
plt.xlabel('b')
plt.ylabel('V')
plt.hold
plt.show()
