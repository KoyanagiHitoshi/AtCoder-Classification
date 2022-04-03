N,X=map(int,input().split())
A=list(map(int,input().split()))
friend=set()
while X not in friend:
	friend.add(X)
	X=A[X-1]
print(len(friend))