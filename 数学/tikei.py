from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
f=open("tikei.csv")
reader=csv.reader(f)
data=[]
tmp=[]
for row in reader:
    data.append(row)
data=np.array(data)
x=range(len(data[0]))
y=range(len(data))
x=np.array(x,dtype=float)
y=np.array(y,dtype=float)

X,Y=np.meshgrid(x,y)
Z=np.array(data,dtype=float)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X,Y,Z,color="#0000FF",rstride=1, cstride=1,linewidth=0.1)
ax.set_zlim(0,3776)

plt.show()
