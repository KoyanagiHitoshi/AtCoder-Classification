n,m=map(int,input().split())
ab=[[int(j) for j in input().split()] for i in range(n)]
cd=[[int(j) for j in input().split()] for i in range(m)]
for a,b in ab:
    l=[abs(a-c)+abs(b-d) for c,d in cd]
    print(l.index(min(l))+1)