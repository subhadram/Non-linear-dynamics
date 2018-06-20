import numpy as n
import pylab as p
import scipy.integrate as integrate

def dr(r, f):
    return a  - r - 4*r*f/1+ r**2
   
	

def df(r, f):
    return b*r*(1 - (f/(1+r**2)))

def derivs(state, t):
    """
    Map the state variable [x, y] to the derivitives
    [deltar, deltaf] at time t
    """
    #print t, state
    r, f = state  # x and y
    deltar = dr(r, f)  # change in x
    deltaf = df(r, f) # change in y
    return deltar, deltaf

a = 5
b = 1

# the initial population of x and y
r0 = 10
f0 = 10

t = n.arange(0.0, 0, 0.1)

y0 = [r0, f0]  # the initial [x, y] state vector
y = integrate.odeint(derivs, y0, t)
r = y[:,0]  # extract the x vector
f = y[:,1]  # extract the y vector

p.figure()
p.plot(t, r, label='x')
p.plot(t, f, label='y')
p.xlabel('t')
p.ylabel('V,w')
p.title('V,w trajectories at b = 1.0, a = 1')
p.grid()
p.legend()
p.savefig('lotka_volterra.png', dpi=150)
p.savefig('lotka_volterra.eps')


p.figure()
p.plot(r, f)
p.xlabel('x',fontsize = 18)
p.ylabel('y',fontsize = 18)
p.title('phase plane')


# make a direction field plot with quiver
#rmax = 1.1 * r.max()
#fmax = 1.1 * f.max()
#rmin = 1.1*r.min()
#fmin = 1.1*f.min()
R, F = n.meshgrid(n.arange(-1,15 , 0.5), n.arange(-1,15 ,0.5))
dR = dr(R, F)
dF = df(R, F)
p.quiver(R, F, dR, dF,linewidths=1)

#qk = p.quiverkey(Q, 0.5, 0.03, 1, "r ,fontproperties={'weight': 'bold'})

#p.plot(X[::3, ::3], Y[::3, ::3], 'k.')
#p.axis([-1, 7, -1, 7])
#p.title("pivot='mid'; every third arrow; units='inches'")



R, F = n.meshgrid(n.arange(-1, 15, .1), n.arange(-1, 15, .1))
dR = dr(R, F)
dF = df(R, F)

p.contour(R, F, dR, levels=[1], linewidths=1, colors='black')
p.contour(R, F, dF, levels=[1], linewidths=1, colors='black')
p.ylabel('y',fontsize = 18)
p.title('trajectory, direction field and null clines of	BZ model at a = 1, b = 1.0',fontsize = 20)

p.savefig('lotka_volterra_pplane.png', dpi=150)
p.savefig('lotka_volterra_pplane.eps')


p.show()

