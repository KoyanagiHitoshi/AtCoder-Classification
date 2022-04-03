N=int(input())
coordinate=[list(map(int,input().split())) for i in range(N)]
print(max(((a[0]-b[0])**2+(a[1]-b[1])**2)**.5 for b in coordinate for a in coordinate))