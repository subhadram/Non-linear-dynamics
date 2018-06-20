import numpy as n
import scipy as s
import pylab as p

xa=0.252
xb=1.99

C=n.linspace(xa,xb,100)
print C
iter=range(1000)
Y = C*0+1
for x in iter:
    Y=Y**2-C

for x in iter:
    Y = Y**2 - C
    p.plot(C,Y, '.', color = 'k', markersize = 2)


p.show()
