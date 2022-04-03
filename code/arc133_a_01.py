N=int(input())
A=list(map(int,input().split()))
x=A[-1]
for i in range(N-1):
	if A[i]>A[i+1]:
		x=A[i]
		break
A=[a for a in A if a!=x]
print(*A)