N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
time=sum(A/B for A,B in AB)/2
dist=0
for A,B in AB:
    dist+=min(A,B*time)
    time-=min(A/B,time)
print(dist)