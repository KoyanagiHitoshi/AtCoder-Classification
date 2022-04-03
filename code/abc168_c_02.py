import math
A,B,H,M=map(int,input().split())
print((A*A+B*B-2*A*B*math.cos(math.radians(abs(30*H-5.5*M))))**.5)