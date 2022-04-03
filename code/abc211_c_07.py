S=input()
c="chokudai"
dp=[1]+[0]*8
for s in S:
    if s in c:
        i=c.index(s)
        dp[i+1]+=dp[i]
        dp[i+1]%=(10**9+7)
print(dp[-1])