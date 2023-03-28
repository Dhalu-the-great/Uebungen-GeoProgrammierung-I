class figur:
    def __init__ (self, name):
        self.name=name
    def umfang(self):
        return 0
    def flaeche(self):
        return 0
    def __str__ (self):
        return f"{self.name}"
    
class punkt (figur):
    def __init__ (self,x,y):
        super().__init__("punkt")
        self.x=x
        self.y=y

    def __sub__ (self,other):
        return vector2(self.x-other.x,self.y-other.y)

    def dist(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

    def __str__ (self):
        return f"[{self.name}, x={self.x}, y={self.y}]"

class vector2(figur):
    def __init__ (self,x,y):
        super().__init__("Vector2")
        self.x=x
        self.y=y
    
    def cross (self,other):
        return ((self.y*other.x-self.x*other.y)**2+(self.x*other.y-self.y*other.x)**2)**0.5
    
class dreieck(figur):
    def __init__(self,Ax,Ay,Bx,By,Cx,Cy):
        super().__init__("Punkt")
        self.A=punkt(Ax,Ay)
        self.B=punkt(Bx,By)
        self.C=punkt(Cx,Cy)

    def flaeche(self):
        v1=(self.B-self.A)
        v2=(self.C-self.A)
        return v1.cross(v2)
        
    def __str__ (self):
        return f"[{self.A}, {self.B}, {self.C}]"

    def umfang(self):
        return self.A.dist(self.B)+self.B.dist(self.B)+self.C.dist(self.A)
p=punkt(1,2)
d=dreieck(1,2,3,4,5,6)

print(d.umfang())
print(d.flaeche())
