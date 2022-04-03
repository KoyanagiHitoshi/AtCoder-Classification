N=int(input())
A=list(map(int,input().split()))
mod=10**9+7
a=[0]*(N+1)
for i in range(N):
    a[i+1]=a[i]+A[i]
ans=0
for i in range(len(A)-1):
    ans+=A[i]*(a[N]-a[i+1])%mod
print(ans%mod)