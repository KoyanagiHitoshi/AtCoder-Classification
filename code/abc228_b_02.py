N,X=map(int,input().split())
A=list(map(int,input().split()))
friend=[]
for i in range(N):
	friend.append(X-1)
	X=A[X-1]
print(len(set(friend)))