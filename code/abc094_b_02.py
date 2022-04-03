N,M,X=map(int,input().split())
A=list(map(int,input().split()))
cost=sum(a>X for a in A)
print(min(cost,M-cost))