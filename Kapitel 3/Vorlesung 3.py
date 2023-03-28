import math
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

    def __str__ (self):
        return f"[{self.name}, x={self.x}, y={self.y}]"
    
class kreis (figur):
    def __init__ (self,m,r):
        super().__init__("kreis")
        self.m=m
        self.r=r
        
    def flaeche(self):
        return self.r**2*math.pi
    
    def umfang(self):
        return self.r*2*math.pi
    def __str__ (self):
        return f"[{self.name}, radius={self.r}, M={self.m}]"



p=punkt(10,5)
k=kreis(p,10)
k.r=20
p.x=20

print(k.name,k.flaeche(),k.umfang())
print(k)