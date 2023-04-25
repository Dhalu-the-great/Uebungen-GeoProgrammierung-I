import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.exp(-x**2) * np.sin(y)


x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)

X, Y = np.meshgrid(x, y)

Z=f(X,Y)
plt.figure(X,Y,Z)
plt.show()