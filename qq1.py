import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

b = np.arange(0,3,0.1)
ymin = []
ymax = []
a = 1.0

def deriv(y, t, a,b):
	r = y[0]
	f = y[1]
	aa = a - (b+1.0)*y[0] + y[1]*y[0]**2
	bb = b*y[0] - y[0]**2*y[1]
	return [aa, bb]

i = 0

for f in b:
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([0.1, 0.1])
	pars = (1.0,f)
	y = odeint(deriv, yinit, time, pars)
	#plt.plot(time,y[:,0], label = f)
	ymin.append(y[-1000:,:].min(axis=0))
	ymax.append(y[-1000:,:].max(axis=0))
	
	
ymin = np.array(ymin)
ymax = np.array(ymax)
    
"""
b = 1.2
for x in np.linspace(0.0,8,40):
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([x,2.0])
	y = odeint(deriv,yinit,time, args=(b,))
	plt.plot(y[:,0],y[:,1])
	
"""	

plt.legend()
plt.plot(b, ymin[:,0], 'g')
plt.plot(b, ymax[:,0], 'g')
plt.plot(b, ymin[:,1], 'b')
plt.plot(b, ymax[:,1], 'b')
plt.xlabel('b')
plt.ylabel('V')
plt.hold
plt.show()
