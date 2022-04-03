N,Q=map(int,input().split())
check=[0]*(N+1)
for i in range(Q):
    l,r=map(int,input().split())
    check[l-1]+=1
    check[r]-=1
for i in range(1,N):
    check[i]+=check[i-1]
othello=""
for i in range(N):
    othello+=str(check[i]%2)
print(othello)