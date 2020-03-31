N=int(input())
NG=[int(input()) for i in range(3)]
dp=[float("INF")]*301
dp[N]=0
for i in range(N,0,-1):
    if i in NG:continue
    for j in range(1,4):
        dp[i-j]=min(dp[i]+1,dp[i-j])
print("YES" if dp[0]<=100 else "NO")