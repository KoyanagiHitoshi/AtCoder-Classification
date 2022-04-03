N,T=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
total=sum(A)
if total<=T:
    print(0)
else:
    cost=[]
    for i in range(N):
        cost.append(B[i]-A[i])
    cost.sort()
    count=-1
    for i in range(N):
        total+=cost[i]
        if total<=T:
            count=i+1
            break
    print(count)