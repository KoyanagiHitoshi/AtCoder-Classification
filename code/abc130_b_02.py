import bisect
N,X=map(int,input().split())
L=list(map(int,input().split()))
for i in range(N-1):L[i+1]+=L[i]
print(bisect.bisect_left(L,X+1)+1)