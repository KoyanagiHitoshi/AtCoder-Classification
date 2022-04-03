import itertools
N,K=map(int,input().split())
T=[list(map(int,input().split())) for i in range(N)]
ans=0
for index in itertools.permutations(range(1,N)):
    index=[0]+list(index)
    time=0
    for i in range(N):
        time+=T[index[i]][index[(i+1)%N]]
    if time==K:
        ans+=1
print(ans)