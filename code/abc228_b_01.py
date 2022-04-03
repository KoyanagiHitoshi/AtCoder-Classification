N,X=map(int,input().split())
A=list(map(int,input().split()))
known=[False]*N
ans=0
for i in range(N):
	known[X-1]=True
	ans+=1
	X=A[X-1]
	if known[X-1]==True:
		break
	else:
		continue
print(ans)