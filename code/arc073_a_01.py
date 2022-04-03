N,T=map(int,input().split())
t=list(map(int,input().split()))
time=0
for i in range(N-1):
    time+=min(t[i+1]-t[i],T)
print(time+T)