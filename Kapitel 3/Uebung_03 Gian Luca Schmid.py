from math import *
class Figur:
    def __init__(self, name):
        self.name = name
        
    def umfang(self):
        return 0
    
    def flaeche(self):
        return 0
    
    def __str__(self):
        return f"{self.name}"

    
class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"[{self.name}, x={self.x}, y={self.y}]"

    
class Vector2(Figur):
    def __init__(self, x, y):
        super().__init__("Vector2")
        self.x = x
        self.y = y
    
    def cross(self, other):
        return abs(self.x * other.y - self.y * other.x)
    
    
class Dreieck(Figur):
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        super().__init__("Dreieck")
        self.A = Punkt(Ax, Ay)
        self.B = Punkt(Bx, By)
        self.C = Punkt(Cx, Cy)

    def flaeche(self):
        v1 = (self.B - self.A)
        v2 = (self.C - self.A)
        return v1.cross(v2) / 2
        
    def __str__(self):
        return f"[{self.A}, {self.B}, {self.C}]"

    def umfang(self):
        return self.A.dist(self.B) + self.B.dist(self.C) + self.C.dist(self.A)

class Rechteck(Figur):
    def __init__(self,ax,ay,bx,by,cx,cy,dx,dy):
        super().__init__("Rechteck")
        self.A = Punkt(ax,ay)
        self.B = Punkt(bx,by)
        self.C = Punkt(cx,cy)
        self.D = Punkt(dx,dy)



    def umfang(self):
        return self.A.dist(self.B)+self.B.dist(self.C)+self.C.dist(self.D)+self.D.dist(self.A)

    def flaeche(self):
        v1 = (self.B - self.A)
        v2 = (self.D - self.A)
        v3 = (self.B - self.C)
        v4 = (self.D - self.C)
        return v1.cross(v2) / 2 + v3.cross(v4)/2

class Kreis (Figur):
    def __init__ (self,mx,my,r):
        super().__init__("Kreis")
        self.m=Punkt(mx,my)
        self.r=r
        
    def flaeche(self):
        return self.r**2*pi
    
    def umfang(self):
        return self.r*2*pi

p = Punkt(1, 2)
d = Dreieck(0, 0, 0, 2, 2, 2)
r=Rechteck(0,0,2,0,2,2,0,2)
k=Kreis(0,0,10)
print(d.umfang())
print(d.flaeche())
print(r.umfang())
print(r.flaeche())
print(k.flaeche())
print(k.umfang())