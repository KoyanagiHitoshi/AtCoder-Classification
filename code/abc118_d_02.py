N,M=map(int,input().split())
A=list(map(int,input().split()))
d=[0]*N*9+[-1]*N*9
for i in range(1,N+1):
    d[i]=max(d[i-int("0255456376"[a])]*10+a for a in A)
print(d[N])