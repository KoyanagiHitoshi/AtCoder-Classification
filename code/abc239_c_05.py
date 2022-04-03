x1,y1,x2,y2=map(int,input().split())
d=(x1-x2)**2+abs(y1-y2)**2
D=[2,4,10,16,18,20]
print("Yes" if d in D else "No")