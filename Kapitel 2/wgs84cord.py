class WGS84coord():
    def __init__ (self,laenge=0,breite=0):
        self.setlong(laenge)
        self.setlat(breite)
    
    def setlong(self,long):
        if long <-180 or long>180:
            raise ValueError("Laege darf nur zwischen -180 und 180 grad sein")
        self._longitude=long

    def setlat(self,lat):
        if lat<-90 or lat >90:
            raise ValueError("Breite darf nur zwischen -90 und 90 grad sein")
        self._latitude=lat

    def getlat(self):
        return self._latitude
    
    def getlong(self):
        return self._longitude

    laenge = property (getlong,setlong)
    breite = property(getlat,setlat)

k1 = WGS84coord(100,69)
print(k1.laenge,k1.breite)

k1.laenge=89
print(k1.laenge,k1.breite)