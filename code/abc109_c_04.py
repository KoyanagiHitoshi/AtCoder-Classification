from fractions import gcd
from functools import reduce
N,D=map(int,input().split())
X=list(map(int,input().split()))
X=sorted(X+[D])
m=min(X)
s=[X[i]-m for i in range(1,len(X))]
print(reduce(gcd,s))