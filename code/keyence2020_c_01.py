N,K,S=map(int,input().split())
A=[S]*N
for i in range(K,N):
    if S==1:
        A[i]=S+1
    else:
        A[i]=S-1
print(*A)