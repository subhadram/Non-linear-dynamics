import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

b = np.arange(0,6,0.1)
ymin = []
ymax = []
#a = 0.0

def deriv(y, t, a,b):
	r = y[0]
	f = y[1]
	aa = a - (b+1.0)*y[0] + y[1]*y[0]**2
	bb = b*y[0] - y[0]**2*y[1]
	return [aa, bb]

i = 0
be = []
for f in b:
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([0.1, 0.1])
	pars = (1,f)
	y = odeint(deriv, yinit, time, pars)
	obe = be
	#plt.plot(time,y[:,1], label = f)
	for i in range(-1000,-1):
		if ((y[i,1]> y[i-1,1])&(y[i,1]> y[i+1,1])):
			ymin.append(y[i,1])
			be.append(f)
		if ((y[i,1]< y[i-1,1])&(y[i,1]< y[i+1,1])):
			ymin.append(y[i,1])
			be.append(f)
	if(len(obe)==len(be)):
		ymin.append(y[-1000:,1].min(axis=0))
		be.append(f)
			

	
	
ymin = np.array(ymin)
be = np.array(be)
    
"""
b = 1.2
for x in np.linspace(0.0,8,40):
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([x,2.0])
	y = odeint(deriv,yinit,time, args=(b,))
	plt.plot(y[:,1],y[:,1])
	
"""	


plt.plot(be, ymin, "b.")
#plt.plot(b, ymax[:,1], label = "Voltage maximum",color = 'blue')
#plt.plot(b, ymin[:,1], 'b')
#plt.plot(b, ymax[:,1], 'b')
plt.xlabel('b' ,fontsize = 18)
plt.ylabel('Y' ,fontsize = 18)
plt.legend()
plt.title("Bifurcation diagram for a = 1 for Brusselator model Y" ,fontsize = 18) 
plt.hold
plt.show()
