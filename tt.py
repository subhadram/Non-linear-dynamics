from numpy import * 
from scipy.integrate import odeint
from pylab import *


a = 1.0
b = 1.0
def dr(x, y):
    return  a - (b+1)*x + x*y**2

def df(x, y):
    return b*y[0] - y[0]**2*y[1]
def deriv(y,t):
	aa = a - (b+1)*y[0] + y[0]*y[1]**2
	bb = b*y[0] - y[0]**2*y[1]
	return array([aa,bb])
	
time = linspace(0.0,100.0,2000)


#fn = -w**2 * sin(x)
yinit = array([1.0,2.0])
y = odeint(deriv,yinit,time)
#figure()
#plot(time,y[:,0])
plot(y[:,0],y[:,1])
r = y[:,0]
f = y[:,1]
rmax = 1.1 * r.max()
fmax = 1.1 * f.max()
R, F =  meshgrid( arange(-1, rmax),  arange(-1, fmax))
dR = dr(R, F)
dF = df(R, F)
quiver(R, F, dR, dF)


R, F =  meshgrid( arange(-1, rmax, .1),  arange(-1, fmax, .1))
dR = dr(R, F)
dF = df(R, F)

contour(R, F, dR, levels=[0], linewidths=3, colors='black')
contour(R, F, dF, levels=[0], linewidths=3, colors='black')
	
	
xlabel('x')
ylabel('y')
show()
	

