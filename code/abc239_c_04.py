x1,y1,x2,y2=map(int,input().split())
d=abs(x1-x2),abs(y1-y2)
D=[(0,2),(0,4),(1,1),(1,3),(2,0),(2,4),(3,1),(3,3),(4,0),(4,2)]
print("Yes" if d in D else "No")