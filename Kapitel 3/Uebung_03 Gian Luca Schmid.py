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


p = Punkt(1, 2)
d = Dreieck(0, 0, 0, 2, 2, 2)

print(d.umfang())
print(d.flaeche())
