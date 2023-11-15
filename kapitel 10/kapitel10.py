from qgis import processing
for alg in QgsApplication.processingRegistry().algorithms():
    print(alg.id(), "->", alg.displayName())
    processing.algorithmHelp("Model:Import and Filter csv")
    