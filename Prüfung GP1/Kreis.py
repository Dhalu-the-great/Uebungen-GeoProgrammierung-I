import matplotlib.pyplot as plt
from math import *
import numpy as np
import matplotlib.patches as patches 
 


class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[x={self.x}, y={self.y}]"

class Kreis ():
    def __init__ (self,mx,my,r):
        self.m=Punkt(mx,my)
        self.r=r

    
    def flaeche(self):
        return self.r**2*pi
    
    def umfang(self):
        return self.r*2*pi
    
    def mittelpunkt (self):
        return self.m
    def draw(self):
        axes = plt.axes() 
 
        circle = patches.Circle((self.m.x,self.m.y), radius=self.r, facecolor=(1,0,0)) 
        axes.add_patch(circle)
        plt.plot(self.m.x,self.m.y, "ko") 
        plt.axis("equal") 
        plt.show() 

    


k=Kreis(5,9,3)
print(k.umfang(),k.flaeche(),k.mittelpunkt())

k.draw()