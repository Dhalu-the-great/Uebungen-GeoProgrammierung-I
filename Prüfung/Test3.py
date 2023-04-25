class koordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class land():
    def __init__ (self,land):
        self.land=land

class kontinent():
    def __init__ (Self,kon):
        Self.kon=kon

class Stadt (koordinate,land,kontinent):
    def __init__ (self,name,einwohner,land,kon,x,y):
        super().__init__(x,y,land,kon)
        self.name=name
        self.einwohner=einwohner

    def __str__ (self):
        return f"{self.name}, {self.einwohner}, {self.land}, {self.kon}, {self.x}, {self.y}"


        

