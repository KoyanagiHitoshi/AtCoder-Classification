N=int(input())
xy=[]
for i in range(N):
    x,y=map(int,input().split())
    xy.append([x,y])
count=0
for i in range(N):
    for j in range(i+1,N):
        if i!=j and -1<=(xy[i][1]-xy[j][1])/(xy[i][0]-xy[j][0])<=1:
            count+=1
print(count)