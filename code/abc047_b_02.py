w,h,n=map(int,input().split())
l=[[int(j) for j in input().split()] for i in range(n)]
b=c=0
for i in range(n):
    x,y,a=l[i][0],l[i][1],l[i][2]
    if a==1:b=max(b,x)
    if a==2:w=min(w,x)
    if a==3:c=max(c,y)
    if a==4:h=min(h,y)
print([(w-b)*(h-c),0][(w<b)|(h<c)])