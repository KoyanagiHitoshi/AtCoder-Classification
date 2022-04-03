N,M=map(int,input().split())
vertex=[list(map(int,input().split())) for i in range(M)]
bridge=0
for a in vertex:
    edge=list(range(N))
    for b in vertex:
        if a!=b:
            edge=[edge[b[0]-1] if edge[i]==edge[b[1]-1] else edge[i] for i in range(N)]
    if len(set(edge))!=1:
        bridge+=1
print(bridge)