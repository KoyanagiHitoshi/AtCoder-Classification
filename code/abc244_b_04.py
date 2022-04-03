N=int(input())
T=input()
x,y,dx,dy=0,0,1,0
for t in T:
    if t=="S":
        x+=dx
        y+=dy
    else:
        dx,dy=dy,-dx
print(x,y)