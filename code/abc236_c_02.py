N,M=map(int,input().split())
S=list(input().split())
T=set(input().split())
for s in S:
	print("Yes" if s in T else "No")