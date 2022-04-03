N,K=map(int,input().split())
p=list(map(int,input().split()))
expection=[0]*N
for i in range(N):
    expection[i]=(p[i]+1)/2
accumulation=[0]*(N+1)
for i in range(N):
    accumulation[i+1]=accumulation[i]+expection[i]
ans=0
for i in range(N-K+1):
    ans=max(ans,accumulation[i+K]-accumulation[i])
print(ans)