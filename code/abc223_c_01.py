N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
time=0
for i in range(N):
    time+=AB[i][0]/AB[i][1]
time/=2
dist=0
i=0
while(time>0):
    dist+=min(AB[i][0],AB[i][1]*time)
    time-=AB[i][0]/AB[i][1]
    i+=1
print(dist)