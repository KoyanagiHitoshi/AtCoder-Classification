N=int(input())
T=input()
x,y,R=0,0,0
for t in list(T):
    if t=="S":
        if R==0: x+=1
        if R==1: y-=1
        if R==2: x-=1
        if R==3: y+=1
    else:
        R=(R+1)%4
print(x,y)