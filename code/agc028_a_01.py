from fractions import gcd
N,M=map(int,input().split())
S=list(input())
T=list(input())
L=gcd(N,M)
n=N//L
m=M//L
print(N*M//L if all([S[i*n]==T[i*m] for i in range(L)]) else "-1")