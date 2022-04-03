N=int(input())
a=list(map(int,input().split()))+[0]
dp=[0]*N
dp[1]=abs(a[1]-a[0])
for i in range(1,N-1):
    dp[i+1]=min(dp[i]+abs(a[i+1]-a[i]),dp[i-1]+abs(a[i+1]-a[i-1]))
print(dp[N-1])