N,K,M=map(int,input().split())
A=list(map(int,input().split()))
x=max(0,M*N-sum(A))
print(x if x<=K else -1)