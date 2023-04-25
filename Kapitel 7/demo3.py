import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.linspace(-np.pi, np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y1, "b-")
plt.plot(x,y2, "k-") # "b" für Blau, g - grün, k - schwarz / "o" für punkte, "x" kreuz / "-" für verbinden, "--" gestrichelt, ":" punkelte linie
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal") #x- und y-Achse gelich gross
plt.show()