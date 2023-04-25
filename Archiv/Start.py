class Punkt:
    def __init__(self,n,sx,sy,sh):
        self.nummer = n
        self.x = sx
        self.y = sy
        self.h = sh

    def hdiff(self,other):
        return abs(self.h-other.h)



p1=Punkt(1,2600000,1200000,540.15)
p2= Punkt(2,0,0,0)
