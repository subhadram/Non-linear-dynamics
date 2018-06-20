from numpy import *
import matplotlib.pylab as plt


statevec={"x1":0.0,"y1":0.0,"z1":0.0,"x2":0.01,"y2":0.01,"z2":0.01}
pardict={"a":0.2,"b":0.2,"c":5.7,"k":0.0}
pardict["k"]=input("Enter the Coupling strength(k):")
def x(index):
	x=statevec["x"+index]
	y=statevec["y"+index]		
	z=statevec["z"+index]
	if index==1:
		a="1"
		b="2"
	else:	
		a="2"
		b="1"
	return(-y-z+(pardict["k"]*(statevec["x"+b]-statevec["x"+a])))		

def y(index):
	x=statevec["x"+index]
	y=statevec["y"+index]
	return(x+(pardict["a"]*y))

def z(index):
	x=statevec["x"+index]
	y=statevec["y"+index]
	z=statevec["z"+index]
	return(pardict["b"]+(z*(x-pardict["c"])))

fundict={"x":x,"y":y,"z":z}
time=500
dt=0.005
t=0

#pop=open(input("Enter file name"),"w")
#pop.write("time\tx1\tx2\n")
observar=("x1","x2")
mat=zeros([(time/dt)+1,len(observar)+1])
temp=statevec
counter=0
while t<time:
	for j in ("1","2"):
		for k in ("x","y","z"):
			temp[k+j]=statevec[k+j]+0.005*fundict[k](j)
	statevec=temp			
	#pop.write(str(t)+"\t"+str(statevec["x1"])+"\t"+str(statevec["x1"])+"\n")
	mat[counter,:]=(t,statevec["x1"],statevec["x2"])
	t=t+dt
	counter=counter+1

#with plt.xkcd():
fig = plt.figure(1)

plt.subplot(311)
plt.plot(mat[:,0],mat[:,1])
plt.xlabel("Time")
plt.ylabel("$x_1$")
plt.subplot(312)
plt.plot(mat[:,0],mat[:,2])
plt.xlabel("Time")
plt.ylabel("$x_2$")
plt.subplot(313)
plt.plot(mat[:,0],mat[:,1]-mat[:,2])
plt.xlabel("Time")
plt.ylabel("$e = x_1-x_2$")
fig.suptitle("Trajectories k = 0.3", fontsize=16)

plt.savefig("rossler_time%.3f.png" %pardict["k"])
#plt.show()
plt.clf()
plt.plot(mat[:,1],mat[:,2])
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("k = 0.3 Phase plane" ,fontsize = 18) 
plt.savefig("rossler_phasplane%.3f.png" %pardict["k"])
plt.clf()
