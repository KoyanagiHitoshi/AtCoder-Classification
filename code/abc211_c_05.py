S=input()
c="chokudai"
dp=[1]+[0]*8
for s in S:
    for i in range(len(c)):
        if s==c[i]:
            dp[i+1]+=dp[i]
            dp[i+1]%=(10**9+7)
print(dp[-1])