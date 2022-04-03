from collections import defaultdict
N,Q=map(int,input().split())
A=list(map(int,input().split()))
a=defaultdict(list)
for i in range(N):
    a[A[i]].append(i+1)
for _ in range(Q):
    x,k=map(int,input().split())
    if k<=len(a[x]):
        print(a[x][k-1])
    else:
        print(-1)