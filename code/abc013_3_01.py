N,H=map(int,input().split())
A,B,C,D,E=map(int,input().split())
ans=C*N
for i in range(N+1):
    cost=(H+B*i+D*(N-i)-1)//(D+E)
    ans=min(ans,A*i+C*max(0,N-i-cost))
print(ans)