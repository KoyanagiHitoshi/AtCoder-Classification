import math
R,X,Y=map(int,input().split())
d=(X**2+Y**2)**.5
print(math.ceil(d/R)+(d<R))