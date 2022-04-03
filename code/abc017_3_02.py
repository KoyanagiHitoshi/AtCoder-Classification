N,M=map(int,input().split())
check=[0]*(M+1)
total=0
for i in range(N):
    l,r,s=map(int,input().split())
    check[l-1]+=s
    check[r]-=s
    total+=s
for i in range(M):
    check[i+1]+=check[i]
print(total-min(check[:-1]))