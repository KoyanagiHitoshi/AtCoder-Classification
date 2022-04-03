from itertools import accumulate
from bisect import bisect_right
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
b=list(accumulate(B))
book=bisect_right(b,K)
for i,a in enumerate(accumulate(A),1):
    if a>K:
        break
    j=bisect_right(b,K-a)
    book=max(book,i+j)
print(book)