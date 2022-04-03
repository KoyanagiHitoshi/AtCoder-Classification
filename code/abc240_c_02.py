N,X=map(int,input().split())
a,b=[0]*N,[0]*N
for i in range(N):
    a[i],b[i]=map(int,input().split())
dp=[[False for i in range(X+1)] for j in range(N+1)]
dp[0][0]=True
for i in range(N):
    for j in range(X+1):
        if dp[i][j]:
            if j+a[i]<=X:
                dp[i+1][j+a[i]]=True
            if j+b[i]<=X:
                dp[i+1][j+b[i]]=True
print("Yes" if dp[N][X] else "No")