dp=[0]*20
dp[0:3]=[100,100,200]
for i in range(3,20):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
print(dp[19])