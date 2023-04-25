import matplotlib.pyplot as plt
from math import *
from random import randint 
import numpy as np


x = np.random.random(1000) * 200 - 100
y = np.random.random(1000) * 200 - 100
colors = np.random.rand(1000)

plt.scatter(x, y, c=colors, cmap='Spectral')
plt.show()