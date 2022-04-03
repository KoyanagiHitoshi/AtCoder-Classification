N,K=map(int,input().split())
p=list(map(int,input().split()))
expected=[0]*N
for i in range(N):
    expected[i]=(p[i]+1)/2
accumurate=[0]*(N+1)
for i in range(1,N+1):
    accumurate[i]=accumurate[i-1]+expected[i-1]
M=0
for i in range(N-K+1):
    M=max(M,accumurate[i+K]-accumurate[i])
print(M)