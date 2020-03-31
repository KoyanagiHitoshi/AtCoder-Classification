A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cost=min(a)+min(b)
for m in range(M):
    x,y,c=map(int,input().split())
    cost=min(cost,a[x-1]+b[y-1]-c)
print(cost)