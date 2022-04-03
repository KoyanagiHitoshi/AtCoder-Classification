N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
time=0
for i in range(N):
    time+=AB[i][0]/AB[i][1]
time/=2
dist=0
for i in range(N):
    dist+=min(AB[i][0],AB[i][1]*time)
    time-=min(AB[i][0]/AB[i][1],time)
print(dist)