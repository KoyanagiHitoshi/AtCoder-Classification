import bisect
N=int(input())
L=sorted(map(int,input().split()))
count=0
for a in range(N-2):
    for b in range(a+1,N-1):
        count+=bisect.bisect_left(L,L[a]+L[b])-(b+1)
print(count)