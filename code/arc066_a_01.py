import math
N=int(input())
A=list(map(int,input().split()))
flag=True
if N%2==0:
    if 0 in A or len(set(A))!=N//2:flag=False
else:
    if len([0 for a in A if a==0])!=1 or len(set(A))!=N//2+1:flag=False
if flag:print(2**(N//2)%(10**9+7))
else:print(0)