N=int(input())
C=sorted(map(int,input().split()))
ans=1
for i in range(N):
    ans=ans*max(0,C[i]-i)%(10**9+7)
print(ans)