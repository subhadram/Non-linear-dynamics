import numpy as np
import matplotlib.pylab as p

a = np.arange(4.5,10.1,0.1)
b = 3*a/5.0 - 25/a
p.plot (a,b)
p.show()

