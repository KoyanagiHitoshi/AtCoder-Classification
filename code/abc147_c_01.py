N=int(input())
testimony=[[-1]*N for i in range(N)]
count=0
for i in range(N):
    A=int(input())
    for j in range(A):
        x,y=map(int,input().split())
        testimony[i][x-1]=y
for i in range(1<<N):
    honest=[0]*N
    for j in range(N):
        if (i>>j)&1:
            honest[j]=1
    flag=True
    for j in range(N):
        if honest[j]:
            for k in range(N):
                if testimony[j][k]==-1:
                    continue
                if testimony[j][k]!=honest[k]:
                    flag=False
    if flag:
        count=max(count,honest.count(1))
print(count)