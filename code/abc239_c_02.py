x1,y1,x2,y2=map(int,input().split())
for x in range(x1-2,x1+3):
    for y in range(y1-2,y1+3):
        if ((x1-x)**2+(y1-y)**2)**.5==((x2-x)**2+(y2-y)**2)**.5==5**.5:
            print("Yes")
            exit()
print("No")