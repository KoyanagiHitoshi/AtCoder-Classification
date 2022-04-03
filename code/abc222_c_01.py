N,M=map(int,input().split())
A=[input() for i in range(2*N)]
rank=[[0,i] for i in range(2*N)]

def judge(a,b):
    if a==b: return -1
    if a=="G" and b=="P": return 1
    if a=="C" and b=="G": return 1
    if a=="P" and b=="C": return 1
    return 0

for m in range(M):
    for n in range(N):
        x=rank[2*n][1]
        y=rank[2*n+1][1]
        result=judge(A[x][m],A[y][m])
        if result!=-1:
            rank[2*n+result][0]-=1
    rank.sort()
for i,j in rank:
    print(j+1)