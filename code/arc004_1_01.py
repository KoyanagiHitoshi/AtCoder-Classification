N=int(input())
p=[]
for i in range(N):
    x,y=map(int,input().split())
    p.append([x,y])
d=0
for i in range(N):
    for j in range(N):
        if i!=j:d=max(d,((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)**.5)
print(d)