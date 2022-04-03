S=input()
c="chokudai"
mod=10**9+7
dp=[[0]*(len(c)+1) for i in range(len(S)+1)]
for i in range(len(S)+1):
    dp[i][0]=1
for i in range(len(S)):
    for j in range(len(c)):
        if S[i]!=c[j]:
            dp[i+1][j+1]=dp[i][j+1]
        if S[i]==c[j]:
            dp[i+1][j+1]=(dp[i][j+1]+dp[i][j])%mod
print(dp[len(S)][8])