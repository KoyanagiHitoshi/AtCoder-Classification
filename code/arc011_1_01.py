m,n,N=map(int,input().split())
ans=N
while N//m>0:
    ans+=N//m*n
    N=N//m*n+N%m
print(ans)