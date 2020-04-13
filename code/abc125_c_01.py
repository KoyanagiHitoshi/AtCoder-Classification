from fractions import gcd
N=int(input())
A=list(map(int,input().split()))
R,L=[0],[0]
for i in range(N-1):
    R+=[gcd(R[i],A[i])]
    L+=[gcd(L[i],A[-i-1])]
print(max(gcd(R[i],L[-i-1]) for i in range(N)))