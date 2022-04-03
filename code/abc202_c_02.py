import collections
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
counter=collections.Counter(A)
ans=0
for c in C:
    ans+=counter[B[c-1]]
print(ans)