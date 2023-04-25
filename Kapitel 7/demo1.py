import matplotlib.pyplot as plt
from math import sin, pi

x=[]
y = []
for i in range(0,101):
    value = i/(100/(4*pi))-2*pi
    x.append(value)
    y.append(sin(value))


plt.plot(x,y, "b-") # "b" für Blau, g - grün, k - schwarz / "o" für punkte, "x" kreuz / "-" für verbinden, "--" gestrichelt, ":" punkelte linie
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal") #x- und y-Achse gelich gross
plt.show()