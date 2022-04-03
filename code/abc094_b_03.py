import bisect
N,M,X=map(int,input().split())
A=list(map(int,input().split()))
cost=bisect.bisect_left(A,X)
print(min(cost,M-cost))