a,b,x,y=map(int,input().split())
move=b-a
if move==0 or move==-1:
    ans=x
elif move<=-2:
    if 2*x<=y:
        ans=(-move-1)*2*x+x
    else:
        ans=(-move-1)*y+x
else:
    if 2*x<=y:
        ans=move*2*x+x
    else:
        ans=move*y+x
print(ans)