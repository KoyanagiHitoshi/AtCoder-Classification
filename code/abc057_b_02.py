import math
N,M=map(int,input().split())
ab=[[int(j) for j in input().split()] for i in range(N)]
cd=[[int(j) for j in input().split()] for i in range(M)]
for i in range(N):
    min_distance=math.inf
    distance=0
    checkpoint=0
    for j in range(M):
        distance=abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
        if distance<min_distance:
            min_distance=distance
            checkpoint=j+1
    print(checkpoint)