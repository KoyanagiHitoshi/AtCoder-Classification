N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
time=sum(A/B for A,B in AB)/2
dist=0
for i in range(N):
    dist+=min(AB[i][0],AB[i][1]*time)
    time-=min(AB[i][0]/AB[i][1],time)
print(dist)