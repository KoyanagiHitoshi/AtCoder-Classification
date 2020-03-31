N,K,M=map(int,input().split())
A=list(map(int,input().split()))
x=M*N-sum(A)
print(max(0,x) if x<=K and x==int(x) else -1)