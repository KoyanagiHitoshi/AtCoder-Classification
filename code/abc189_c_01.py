N=int(input())
A=list(map(int,input().split()))
ans=0
for l in range(N):
    y=max(A)
    for r in range(l,N):
        x=r-l+1
        y=min(y,A[r])
        eat=x*y
        ans=max(ans,eat)
print(ans)