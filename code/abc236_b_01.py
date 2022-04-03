N=int(input())
A=list(map(int,input().split()))
ans=0
for a in A:
	ans=ans^a
print(ans)