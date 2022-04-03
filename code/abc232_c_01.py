import itertools
N,M=map(int,input().split())
A=[[False]*N for _ in range(N)]
B=[[False]*N for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    A[u][v]=A[v][u]=True
for _ in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    B[u][v]=B[v][u]=True
ans=False
for p in itertools.permutations(range(N)):
    ok=True
    for i in range(N):
        for j in range(N):
            if A[i][j]!=B[p[i]][p[j]]:
                ok=False
    if ok:
        ans=True
print("Yes" if ans else "No")