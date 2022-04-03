import math
a,b,x=map(int,input().split())
volume=a*a*b
if volume>=2*x:
    theta=(a*b*b)/(2*x)
else:
    theta=2*(volume-x)/(a*a*a)
print(math.degrees(math.atan(theta)))