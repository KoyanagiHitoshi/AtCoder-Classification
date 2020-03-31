N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]
AB.sort()
ans=0
count=0
for i in range(N):
    count=M-AB[i][1]
    if count>=0:
        ans+=AB[i][0]*AB[i][1]
        M=count
    else:
        ans+=AB[i][0]*M
        break
print(ans)