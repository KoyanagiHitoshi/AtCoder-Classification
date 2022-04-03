import itertools
N,K=map(int,input().split())
T=[list(map(int,input().split())) for i in range(N)]
ans=0
for p in itertools.permutations(range(1,N)):
    time=0
    visited=0
    for i in range(N-1):
        city=p[i]
        time+=T[visited][city]
        visited=city
    time+=T[visited][0]
    if time==K:
        ans+=1
print(ans)