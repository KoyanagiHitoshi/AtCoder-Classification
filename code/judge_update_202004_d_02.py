from math import gcd
N,Q=map(int,input().split())
A=list(map(int,input().split()))
S=list(map(int,input().split()))
accumulation=[A[0]]
for i in range(N-1):
    accumulation.append(gcd(A[i+1],accumulation[i]))
for i in range(Q):
    if gcd(S[i],accumulation[N-1])!=1:
        print(gcd(S[i],accumulation[N-1]))
    else:
        ok=N-1
        ng=-1
        while ok-ng>1:
            mid=(ok+ng)//2
            if gcd(accumulation[mid],S[i])==1:
                ok=mid
            else:
                ng=mid
        print(ok+1)