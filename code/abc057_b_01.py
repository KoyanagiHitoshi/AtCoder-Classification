N,M=map(int,input().split())
ab=[[int(j) for j in input().split()] for i in range(N)]
cd=[[int(j) for j in input().split()] for i in range(M)]
for a,b in ab:
    distance=[abs(a-c)+abs(b-d) for c,d in cd]
    print(distance.index(min(distance))+1)