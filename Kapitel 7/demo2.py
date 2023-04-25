import numpy as np

a = np.array([1,2,3,4], dtype=np.float64)

print(a*a)

b = np.array([[1,2,3],[4,5,6]])

if 50 in b:
    print("5 kommt in der matrix b for")
else:
    print("5 kommt nicht for")

print(b[0,:])  # 1 Zeile in der Martix
print(b[:,1])  # 2 Linie in der Martix

c = np.zeros([4,4])
c[0,1] =5
print(c)

d = np.arange(-2*np.pi,2*np.pi+0.1,0.1) 
print(d)

e = np.linspace(0,1,11) # von 0 bis 1 mit 11 Werte zwischen
print(e)

f = np.random.random(20) # Linte mit 20 zufällige Zahlen zwischen 0 und 1
print(f)