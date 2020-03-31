N,K,M=map(int,input().split())
A=sum(map(int,input().split()))
x=max(0,M*N-A)
print(x if x<=K else -1)