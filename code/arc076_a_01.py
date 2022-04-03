import math
N,M=map(int,input().split())
print(max(2-abs(N-M),0)*math.factorial(N)*math.factorial(M)%(10**9+7))