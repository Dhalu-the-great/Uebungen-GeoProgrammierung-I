import numpy as np
import matplotlib.pyplot as plt



def f(x, y):
    return np.exp(-x**2) * np.sin(y)


x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)

X, Y = np.meshgrid(x, y)

Z=f(X,Y)

plt.pcolormesh(X,Y,Z )
plt.colorbar()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

plt.show()