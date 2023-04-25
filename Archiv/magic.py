class punkt:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"[{self.x},{self.y}]"
    
    def __gt__ (self,other):
        return self.c > other.c
    
    def __lt__ (self,other):
        return self.c < other.c
    
    def __eq__ (self,other):
        return self.c == other.c

class vector3:
    def __init__ (self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"[{self.x},{self.y},{self.z}]"

    def __add__ (self,other):
        return vector3(self.x + other.x , self.y + other.y,self.z+other.z)
    
    def __sub__(self,other):
        return vector3(self.x - other.x , self.y - other.y, self.z-other.z)
    
    def __mul__ (self,other):
        if type(other)==vector3:
            return vector3(self.x*other.x,self.y*other.y,self.z*other.z)
        elif type(other)== float or type(other)== int:
            return vector3(other*self.x,other*self.y,other*self.z)

    def __rmul__ (self, other):
         return vector3(other*self.x,other*self.y,other*self.z)
    
    def dot (self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def cross (self,other):
        return vector3(self.y*other.z-self.z*other.y,
                       self.z*other.x-self.x*other.z,
                       self.x*other.y-self.y*other.x)
    
    def normalize (self):
        value = (self.x**2+self.y**2+self.z**2)**(1/2)
        return vector3(self.x/value,self.y/value,self.z/value)

    def __truediv__ (self,other):
        return vector3(self.x/other.x,self.y/other.y,self.z/other.z)
    def __neg__(self):
        return vector3(-self.x,-self.y,-self.z)
    

    

v1=vector3(1,2,3)
v2=vector3(3,4,5)
v3=v1+v2
v4=v1+v3
v5=v4.normalize()
v6=v4.cross(v3)
print(v6)