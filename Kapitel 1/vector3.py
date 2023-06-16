class Vector3():
    def __init__(self,x=None,y=None,z=None):
        self.x=x
        self.y=y
        self.z=z
        if x==None and y==None and z==None:
            self.x=0
            self.y=0
            self.z=0

    def len(self):
        return((self.x)**2+(self.y)**2+(self.z)**2)**0.5

v1=Vector3(3,5,9)
print(v1.len())
