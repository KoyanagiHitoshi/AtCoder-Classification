from fractions import gcd
from functools import reduce
N,X=map(int,input().split())
x=[abs(X-i) for i in map(int,input().split())]
print(reduce(gcd,x))