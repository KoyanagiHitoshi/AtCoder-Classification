import collections
N=int(input())
A=collections.Counter(list(map(int,input().split())))
ans=0
for a in A:
    N-=A[a]
    ans+=N*A[a]
print(ans)