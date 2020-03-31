N=int(input())
txy=[list(map(int,input().split())) for i in range(N)]
ans=0
for i in range(N):
    t,x,y=txy[i][0],txy[i][1],txy[i][2]
    if x+y<=t and t%2==(x+y)%2:ans+=1
print("Yes" if ans==N else "No")