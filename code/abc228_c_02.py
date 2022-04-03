N,K=map(int,input().split())
P=[sum(map(int,input().split())) for i in range(N)]
line=sorted(P)[-K]
print(*["Yes" if p>=line-300 else "No" for p in P],sep="\n")