N,M,X=map(int,input().split())
CA=[list(map(int,input().split())) for i in range(N)]
min_cost=float("inf")
for bit in range(1<<N):
    cost=0
    understand=[0]*M
    for digit in range(N):
        if (bit>>digit)&1:
            cost+=CA[digit][0]
            for m in range(M):
                understand[m]+=CA[digit][m+1]
    if all(understand[m]>=X for m in range(M)):
        min_cost=min(min_cost,cost)
print(min_cost if min_cost!=float("inf") else -1)