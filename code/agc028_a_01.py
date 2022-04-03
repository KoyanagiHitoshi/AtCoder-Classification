import math
N,M=map(int,input().split())
S=list(input())
T=list(input())
L=math.gcd(N,M)
print(N*M//L if all([S[i*N//L]==T[i*M//L] for i in range(L)]) else "-1")