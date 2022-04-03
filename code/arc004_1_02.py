import math
N=int(input())
coordinate=[list(map(int,input().split())) for i in range(N)]
print(max(math.hypot(a[0]-b[0],a[1]-b[1]) for b in coordinate for a in coordinate))