N,M,X=map(int,input().split())
CA=[list(map(int,input().split())) for i in range(N)]
costs=[]
for bit in range(1<<N):
    cost=0
    understand=[0]*M
    for digit in range(N):
        if (bit>>digit)&1:
            cost+=CA[digit][0]
            for m in range(M):
                understand[m]+=CA[digit][m+1]
    if all(understand[m]>=X for m in range(M)):
        costs.append(cost)
print(min(costs) if costs else -1)