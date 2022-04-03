N=int(input())
coordinate=[]
for i in range(N):
    x,y=map(int,input().split())
    coordinate.append([x,y])
distance=0
for i in range(N):
    for j in range(N):
        if i!=j:
            distance=max(distance,((coordinate[i][0]-coordinate[j][0])**2+(coordinate[i][1]-coordinate[j][1])**2)**.5)
print(distance)