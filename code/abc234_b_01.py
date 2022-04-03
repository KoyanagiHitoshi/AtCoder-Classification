N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
ans=0
dist=0
for a in range(N):
	for b in range(N):
		dist=max(dist,((xy[a][0]-xy[b][0])**2+(xy[a][1]-xy[b][1])**2)**.5)
print(dist)