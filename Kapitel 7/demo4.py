import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.linspace(-np.pi, np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)


fig, ax = plt.subplots(2) #kann mehr dimensional mit Z.b.(2,2)
ax[0].plot(x,y1, "b-")
ax[1].plot(x,y2, "k-") # "b" für Blau, g - grün, k - schwarz / "o" für punkte, "x" kreuz / "-" für verbinden, "--" gestrichelt, ":" punkelte linie



plt.show()