import numpy as n
import pylab as p
import scipy.integrate as integrate

def dr(r, f):
	return a - (b+1.0)*r + f*r**2
	
	

def df(r, f):
    return  b*r - f**2*f

def derivs(state, t):
    """
    Map the state variable [rabbits, foxes] to the derivitives
    [deltar, deltaf] at time t
    """
    #print t, state
    r, f = state  # rabbits and foxes
    deltar = dr(r, f)  # change in rabbits
    deltaf = df(r, f) # change in foxes
    return deltar, deltaf

a = 1
b = 3



t = n.arange(0.0, 10, 0.1)
for x in n.linspace(0.0,5,5):
	for z in n.linspace(0.0, 2.0,5):
		yinit = n.array([x,z])
		y = integrate.odeint(derivs,yinit,t)
		#figure()
		#plot(time,y[:,0])
		p.plot(y[:,0],y[:,1], alpha = 0.5)
  

r = y[:,0]  
f = y[:,1]  # extract the foxes vector


#p.figure()
p.plot(r, f)
p.xlabel('X',fontsize = 18)
p.ylabel('Y',fontsize = 18)
#p.title('phase plane')


# make a direction field plot with quiver
rmax = 1.1 * r.max()
fmax = 1.1 * f.max()
#R, F = n.meshgrid(n.arange(-1, rmax,0.1), n.arange(-1, fmax,0.1))
R, F = n.meshgrid(n.arange(0,100, .1), n.arange(0, 100, .1))
dR = dr(R, F)
dF = df(R, F)
#p.quiver(R, F, dR, dF)


R, F = n.meshgrid(n.arange(0,100, .1), n.arange(0, 100, .1))
dR = dr(R, F)
dF = df(R, F)

p.contour(R, F, dR, levels=[0], linewidths=3, colors='blue', label = "X nullcline")
p.contour(R, F, dF, levels=[0], linewidths=3, colors='green', label = "Y nullcline")
p.legend()
p.title('Nullclines, phase phase flow and trajectories for Brusselator model. a = 1, b = 1',fontsize = 18)


p.show()
