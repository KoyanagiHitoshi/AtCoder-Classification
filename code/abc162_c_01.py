import math
K=int(input())
print(sum(math.gcd(math.gcd(a,b),c) for a in range(1,K+1) for b in range(1,K+1) for c in (range(1,K+1))))