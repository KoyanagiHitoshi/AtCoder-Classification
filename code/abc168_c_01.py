import math
A,B,H,M=map(int,input().split())
print((A**2+B**2-2*A*B*math.cos(2*(H/12+M/60/12-M/60)*math.pi))**.5)