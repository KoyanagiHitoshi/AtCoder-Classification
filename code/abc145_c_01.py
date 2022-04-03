N=int(input())
xy=[list(map(int,input().split())) for i in range(N)]
print(sum(((xi-xj)**2+(yi-yj)**2)**.5 for xi,yi in xy for xj,yj in xy)/N)