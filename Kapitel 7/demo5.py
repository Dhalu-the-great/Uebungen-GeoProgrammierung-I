import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

ax = plt.axes()

kreis = patches.Circle((0,0), radius = 1.0, fc=(1,0,0), ec= (0,0,0) , lw = 5) 
ax.add_patch(kreis)
plt.axis("equal")

plt.show()