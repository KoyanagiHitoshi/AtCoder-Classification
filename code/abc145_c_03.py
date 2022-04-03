N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
distance=0
for xi,yi in xy:
    for xj,yj in xy:
        distance+=((xi-xj)**2+(yi-yj)**2)**.5
print(distance/N)