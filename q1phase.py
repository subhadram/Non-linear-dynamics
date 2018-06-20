from numpy import * 
from scipy.integrate import odeint
from pylab import *


a = 0.1
b = 0.1
c = 9
def deriv(y,t):
	x = y[0]
	w = y[1]
	z = y[2]
	dy0 = -w -z
	dy1 = x +a*w
	dy2 = b+z*(x-c)
	return array([dy0,dy1,dy2])
	
time = linspace(0.0,1000.0,20000)


yinit = array([1.0,2.0,1.0])
y = odeint(deriv,yinit,time)
#figure()
#plot(time,y[:,0])
plot(y[-5000:-1,0],y[-5000:-1,1])
	
	
xlabel('x')
ylabel('y')
title('Phase space for c = 9')
show()
	

