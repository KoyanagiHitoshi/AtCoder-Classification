N,M=map(int,input().split())
edges=[list(map(int,input().split())) for i in range(M)]
ans=0
for x in edges:
    l=list(range(N))
    for y in edges:
        if y!=x:l=[l[y[0]-1] if l[i]==l[y[1]-1] else l[i] for i in range(N)]
    if len(set(l))!=1:ans+=1
print(ans)