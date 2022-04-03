N,X=map(int,input().split())
A=list(map(int,input().split()))
friend=set()
for i in range(N):
	friend.add(X-1)
	X=A[X-1]
print(len(friend))