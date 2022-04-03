N,K=map(int,input().split())
A=list(map(int,input().split()))
num=[0]*N
for a in A:
    num[a]+=1
ans=0
value=[0]*N
value[0]=min(K,num[0])
ans+=value[0]
for i in range(1,N):
    value[i]=min(K,value[i-1],num[i])
    ans+=value[i]
print(ans)