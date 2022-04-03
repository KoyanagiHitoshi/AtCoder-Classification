N,L,W=map(int,input().split())
A=list(map(int,input().split()))+[L]
ans,r=0,0
for a in A:
    if a>r:
        ans+=(a-r+W-1)//W
    r=a+W
print(ans)