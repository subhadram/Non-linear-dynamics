import numpy as n
import pylab as p
import scipy.integrate as integrate

def dr(r, f):
    return a - (b+1)*r + r**2*f
	

def df(r, f):
    return b*r - r**2*f

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

a = 1.0
b = 3.0

# the initial population of x and y
r0 = 1
f0 = 1

t = n.arange(0.0, 100, 0.1)

y0 = [r0, f0]  # the initial [x, y] state vector
y = integrate.odeint(derivs, y0, t)
r = y[:,0]  # extract the x vector
f = y[:,1]  # extract the y vector

p.figure()
p.plot(t, r, label='x')
p.plot(t, f, label='y')
p.xlabel('t')
p.ylabel('x,y')
p.title('x,y trajectories at b = 3.0, a = 1')
p.grid()
p.legend()
p.savefig('lotka_volterra.png', dpi=150)
p.savefig('lotka_volterra.eps')


p.figure()
p.plot(r, f)
p.xlabel('x')
p.ylabel('y')
p.title('phase plane')


# make a direction field plot with quiver
rmax = 1.1 * r.max()
fmax = 1.1 * f.max()
R, F = n.meshgrid(n.arange(0, rmax, .05), n.arange(0, fmax,.05))
dR = dr(R, F)
dF = df(R, F)
p.quiver(R, F, dR, dF)
qk = p.quiverkey(R,F, 0.03, 1, r'$1 \frac{m}{s}$',
                   fontproperties={'weight': 'bold'})


R, F = n.meshgrid(n.arange(0, rmax, .1), n.arange(0, fmax, .1))
dR = dr(R, F)
dF = df(R, F)

p.contour(R, F, dR, levels=[0], linewidths=1, colors='black')
p.contour(R, F, dF, levels=[0], linewidths=1, colors='black')
p.ylabel('y')
p.title('trajectory, direction field and null clines of Brusselator model at a = 1, b = 3.0')

p.savefig('lotka_volterra_pplane.png', dpi=150)
p.savefig('lotka_volterra_pplane.eps')


p.show()

