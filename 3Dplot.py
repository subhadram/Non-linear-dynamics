from numpy import * 
from scipy.integrate import odeint
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


s = 10
g = 1.5
b = 28
def deriv(y,t):
	r = y[0]
	f = y[1]
	h = y[2]
	aa = s*(f-r)
	bb = g*r -f -r*h
	cc= r*f -b*h
	return array([aa,bb,cc])
	
time = linspace(0.0,200.0,2000)


yinit = array([1,1,1])
y = odeint(deriv,yinit,time)
plot(time,y[:,0])
#Axes3D.plot(y[:,0],y[:,1]),y[:,2])	
#Axes3D.plot_wireframe(y[:,0],y[:,1]),y[:,2])
#Axes3D.scatter(y[:,0],y[:,1]),y[:,2]), zdir='z', s=20, c='b', depthshade=True, *args, **kwargs)	
xlabel('x')
ylabel('y')
show()
	

