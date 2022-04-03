N=int(input())
P=list(map(int,input().split()))
Q=[0]*N
for i,p in enumerate(P):
    Q[p-1]=i+1
print(*Q)