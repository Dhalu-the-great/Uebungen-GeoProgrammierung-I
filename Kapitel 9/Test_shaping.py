import shapely
from shapely.geometry import Point,Polygon,MultiPoint
from shapely import wkt
import matplotlib.pyplot as plt


Muttenz = Point([7.642408447,5347037])


print(Muttenz.wkt)

wkt1 = "POLYGON (( -5 -5, 5 -5, 5 5, -5 5, -5 -5))"
wkt2 = "POLYGON ((1 -1, 4 -1, 4 1, 1 1, 1 4, -1 4, -1 1, -4 1, -4 -1, -1 -1, -1 -4, 1 -4, 1 -1))"

g1=shapely.wkt.loads(wkt1)    
g2=shapely.wkt.loads(wkt2)


x,y = g2.exterior.xy
plt.plot(x,y,"r-")
x,y=g1.exterior.xy
plt.plot(x,y,"b-")
plt.axis("equal")



differenz =g1.difference(g2)
print(differenz)


print("EXTERIOR",differenz.exterior)
print("INTERIOR",differenz.interiors[0])

plt.show()