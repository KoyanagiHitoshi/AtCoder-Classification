N=int(input())
XY=[tuple(map(int,input().split())) for i in range(N)]
for i in range(N):
    for j in range(i):
        for k in range(j):
            x1,y1=XY[i]
            x2,y2=XY[j]
            x3,y3=XY[k]
            x1-=x3
            x2-=x3
            y1-=y3
            y2-=y3
            if x1*y2==x2*y1:
                print("Yes")
                exit()
print("No")