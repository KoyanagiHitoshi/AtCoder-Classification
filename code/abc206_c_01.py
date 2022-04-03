import collections
N=int(input())
A=list(map(int,input().split()))
counter=collections.Counter(A)
ans=0
for i in range(N):
    ans+=N-i-counter[A[i]]
    counter[A[i]]-=1
print(ans)