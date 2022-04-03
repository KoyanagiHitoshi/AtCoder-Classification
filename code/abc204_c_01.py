import sys
sys.setrecursionlimit(10000)
N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    G[A-1].append(B-1)
def dfs(v):
    if tmp[v]:
        return
    tmp[v]=True
    for vv in G[v]:
        dfs(vv)
ans=0
for i in range(N):
    tmp=[False]*N
    dfs(i)
    ans+=sum(tmp)
print(ans)