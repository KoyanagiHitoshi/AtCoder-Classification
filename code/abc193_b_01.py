N=int(input())
MAX=10**9
cost=MAX
for i in range(N):
    A,P,X=map(int,input().split())
    if X-A>0:
        cost=min(cost,P)
print(cost if cost!=MAX else -1)