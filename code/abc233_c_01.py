from collections import defaultdict
N,X=map(int,input().split())
DP=defaultdict(int)
DP[1]=1
for i in range(N):
    L,*A=map(int,input().split())
    E=DP.copy()
    DP=defaultdict(int)
    for a in A:
        for Y in E:
            DP[Y*a]+=E[Y]
print(DP[X])