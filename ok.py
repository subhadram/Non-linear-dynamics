from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
ion()

def RM(y, t, r, K, a, h, e, d):
    return array([ y[0] * ( r*(1-y[0]/K) - a*y[1]/(1+a*h*y[0]) ),
                   y[1] * (e*a*y[0]/(1+a*h*y[0]) - d) ])

t = arange(0, 1000, .1)
y0 = [1, 1.]
pars =  (1., 10., 1., 0.1, 0.1, 0.1)

y = odeint(RM, y0, t, pars)
plot(t, y)
xlabel('time')
ylabel('population')
legend(['resource', 'consumer'])
