N=int(input())
cost=-1
for i in range(N):
    A,P,X=map(int,input().split())
    if X-A>0 and (cost==-1 or P<cost):
        cost=P
print(cost)