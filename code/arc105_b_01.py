import math
N=int(input())
A=list(map(int,input().split()))
res=0
for a in A:
    res=math.gcd(res,a)
print(res)