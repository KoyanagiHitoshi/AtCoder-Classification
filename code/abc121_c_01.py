N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda AB:(AB[0],AB[1]))
ans=0
count=0
for i in range(N):
    count=M-AB[i][1]
    if count>=0:
        ans+=AB[i][0]*AB[i][1]
        M=M-AB[i][1]
    else:
        ans+=AB[i][0]*M
        break
print(ans)