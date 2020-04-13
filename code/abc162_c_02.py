import math
K=int(input())
r=range(1,K+1)
print(sum(math.gcd(math.gcd(a,b),c) for a in r for b in r for c in r))