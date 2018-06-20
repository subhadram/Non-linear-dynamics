from numpy import * 
from scipy.integrate import odeint
from pylab import *


a = 1.0
b = 3.0
def deriv(y,t):
	aa = a - (b+1.0)*y[0] + y[1]*y[0]**2
	bb = b*y[0] - y[0]**2*y[1]
	return array([aa,bb])
	
time = linspace(0.0,1000.0,2000)

for x in linspace(0.0,8,1):
	#fn = -w**2 * sin(x)
	yinit = array([x,2.0])
	y = odeint(deriv,yinit,time)
	figure()
	plot(time,y[:,0])
	#plot(y[:,0],y[:,1])
	
	
xlabel('x')
ylabel('y')
show()
	

