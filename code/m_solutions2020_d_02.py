N=int(input())
A=list(map(int,input().split()))
dp=[0]*N
dp[0]=1000
for i in range(1,N):
    dp[i]=max(dp[i-1],dp[i-1]//A[i-1]*A[i]+dp[i-1]%A[i-1])
print(dp[-1])