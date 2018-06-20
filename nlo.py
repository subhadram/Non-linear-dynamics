from numpy import * 
from scipy.integrate import odeint
from pylab import *


k = 0.5
w = 1.0
def deriv(y,t):
	a = y[1]
	b = -w**2 * sin(y[0]) - k*y[1]
	return array([a,b])
	
time = linspace(0.0,20.0,2000)

for x in linspace(0.0,8,40):
	fn = -w**2 * sin(x)
	yinit = array([x,2.0])
	y = odeint(deriv,yinit,time)
	#figure()
	#plot(time,y[:,0])
	plot(y[:,0],y[:,1])
	
	
xlabel('x')
ylabel('y')
show()
	

