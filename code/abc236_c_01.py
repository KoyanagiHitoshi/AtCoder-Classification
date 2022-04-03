N,M=map(int,input().split())
S=list(input().split())
T=set(input().split())
for s in S:
	if s in T:
		print("Yes")
		T.remove(s)
	else:
		print("No")