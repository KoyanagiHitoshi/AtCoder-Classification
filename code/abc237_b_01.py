H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
for a in zip(*A):
	print(*a)