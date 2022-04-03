N,M=map(int,input().split())
edges=[set() for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)
for i in range(N):
    print(len({n for v in edges[i] for n in edges[v] if not n in edges[i] and n!=i}))