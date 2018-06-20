import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
s=10
r=5
b=2.667
def lorenz(w,t):
	x = w[0]
	y = w[1]
	z = w[2]
	x_dot = s*(y - x)
	y_dot = r*x - y - x*z
	z_dot = x*y - b*z
	return np.array([ x_dot, y_dot, z_dot])

time = np.linspace(0.0,2000.0,200000)

fig = plt.figure()

ax = fig.gca(projection='3d')
for x in np.linspace(-2,2,2):
	for p in np.linspace(1,2,2):
		for y in np.linspace(1,2,2):
			yinit = np.array([x,y,p])
			y = odeint(lorenz,yinit,time)
			ax.plot(y[:,0], y[:,1], y[:,2])



#fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax.plot(xs, ys, zs)
ax.set_xlabel("X Axis")
#ax.set_zlim(0,2)
#ax.set_xlim(-2,2)
#ax.set_ylim(-2,2)
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title(r"$Lorenz\ Attractor\ at\ \gamma = 5$")

plt.show()
