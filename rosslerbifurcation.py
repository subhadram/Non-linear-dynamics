import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

c = np.arange(0,35,0.1)
ymin = []
ymax = []
#a = 0.0

def deriv(y, t, a,b,c):
	r = y[0]
	f = y[1]
	h = y[2]
	aa = -f-h
	bb = r +a*f
	cc= b+h*(r-c)
	return [aa, bb, cc]

i = 0
be = []
for f in c:
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([0.1, 0.1,0.1])
	pars = (0.1,0.1,f)
	y = odeint(deriv, yinit, time, pars)
	obe = be
	#plt.plot(time,y[:,0], label = f)
	for i in range(-1000,-1):
		if ((y[i,0]> y[i-1,0])&(y[i,0]> y[i+1,0])):
			ymin.append(y[i,0])
			be.append(f)
		#if ((y[i,0]< y[i-1,0])&(y[i,0]< y[i+1,0])):
		#	ymin.append(y[i,0])
		#	be.append(f)
	if(len(obe)==len(be)):
		ymin.append(y[-1000:,0].min(axis=0))
		be.append(f)
			

	
	
ymin = np.array(ymin)
be = np.array(be)
    
"""
b = 1.2
for x in np.linspace(0.0,8,40):
	time = np.arange(0.0, 2000,0.01)
	yinit = np.array([x,2.0])
	y = odeint(deriv,yinit,time, args=(b,))
	plt.plot(y[:,0],y[:,0])
	
"""	


plt.plot(be, ymin, "r.")
#plt.plot(b, ymax[:,0], label = "Voltage maximum",color = 'blue')
#plt.plot(b, ymin[:,0], 'b')
#plt.plot(b, ymax[:,0], 'b')
plt.xlabel('c' ,fontsize = 18)
plt.ylabel('x' ,fontsize = 18)
plt.legend()
plt.title("Bifurcation diagram for a = b = 0.1 Rossler system" ,fontsize = 18) 
plt.hold
plt.show()
