class person():
    def __init__(self,Name="Hans-Peter",Alter=35,Adresse="FHNW"):
        self.name=Name
        self.alter=Alter
        self.adresse=Adresse

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}, Adresse: {self.adresse}"
    
    def print_info(self):
        print("Name: "+str(self.name)+", Alter: "+str(self.alter)+", Adresse: "+str(self.adresse))

fabian=person("Gross Fabian",21,"Hofackerstrasse 7")
fabian.print_info()
print(fabian)


class V2():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__ (self,other):
        return V2(self.x-other.x,self.y-other.y)
    
    def __add__ (self,other):
        return V2(self.x+other.x,self.y+other.y)
    
    def __str__ (self):
        return f"X={self.x},Y={self.y}"

v1=V2(3,5)
v2=V2(7,9)
v3=v1-v2
v4=v3+v2

print(v3,v4)


class Shape():
    def __init__ (self,Name):
        self.name=Name
        def area(self):
            return None
        def umfang (self):
            return None
        def __str__ (self):
            return f"{self.name}"


class Rechteck(Shape):
    def __init__(self,x1,x2,y1,y2):
        super().__init__("Rechteck")
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def area (self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    

r1=Rechteck(2,4,3,6)
print(r1.area())


