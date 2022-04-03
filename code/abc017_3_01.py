N,M=map(int,input().split())
imos=[0]*(M+1)
total=0
for i in range(N):
    l,r,s=map(int,input().split())
    imos[l-1]+=s
    imos[r]-=s
    total+=s
for i in range(M):
    imos[i+1]+=imos[i]
print(total-min(imos[:-1]))