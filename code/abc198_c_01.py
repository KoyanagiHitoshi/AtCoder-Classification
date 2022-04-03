import math
R,X,Y=map(int,input().split())
d=(X**2+Y**2)**.5
print(1 if d==R else 2 if d<=2*R else math.ceil(d/R))