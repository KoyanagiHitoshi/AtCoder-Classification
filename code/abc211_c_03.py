S=input()
dp=[1]+[0]*8
for s in S:
    i="chokudai".find(s)
    if i>=0:
        dp[i+1]+=dp[i]
        dp[i+1]%=(10**9+7)
print(dp[-1])