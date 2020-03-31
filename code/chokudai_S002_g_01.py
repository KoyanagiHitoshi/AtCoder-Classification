from functools import reduce
from fractions import gcd
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(gcd(a,b))