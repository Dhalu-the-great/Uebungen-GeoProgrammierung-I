
from skimage import data
from skimage import io
from skimage import util
from skimage import filters
from skimage import color
import numpy as np
import matplotlib.pyplot as plt

b1=data.coffee()
b2=b1[:,:,:]
b3=color.rgb2hsv(b1)
b4=b3[:,:,2]
b5=b4[:,100:400]
io.imshow(b5)
io.show()
print(b1)