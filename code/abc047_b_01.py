W,H,N=map(int,input().split())
width=height=0
for i in range(N):
    x,y,a=map(int,input().split())
    if a==1:
        width=max(width,x)
    if a==2:
        W=min(W,x)
    if a==3:
        height=max(height,y)
    if a==4:
        H=min(H,y)
print(max(0,(W-width))*max(0,(H-height)))