N,K,M=map(int,input().split())
A=list(map(int,input().split()))
point=max(0,M*N-sum(A))
print(point if point<=K else -1)