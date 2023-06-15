from qgis.core import *
import qgis.utils

canvas = iface.mapCanvas()
layers = canvas.layers()

features = airports.getFeatures()
alles=list(features)
file=open("C:/Users/doese/Documents/GitHub/Uebungen-GeoProgrammierung-I/kapitel 10/airports.csv","w",encoding="utf-8")
for data in alles:
    name = data.attributes()[4]
    wikipedia = data.attributes()[9]
    geometrie = data.geometry().asPoint()
    file.write(f"{name},{wikipedia},{geometrie.x()},{geometrie.y()}\n")
    
file.close()
print("done")
