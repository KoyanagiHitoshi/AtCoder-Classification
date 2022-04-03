from itertools import accumulate
from bisect import bisect_right
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=list(accumulate(A))
b=list(accumulate(B))
book=bisect_right(b,K)
for i in range(N):
    if a[i]>K:
        break
    j=bisect_right(b,K-a[i])
    book=max(book,(i+1)+j)
print(book)