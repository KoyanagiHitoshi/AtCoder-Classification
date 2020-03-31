N=int(input())
B=list(map(int,input().split()))
B+=[max(B)]
A=[0]*N
A[0]=B[0]
for i in range(1,N):
    A[i]=min(B[i-1],B[i])
print(sum(A))