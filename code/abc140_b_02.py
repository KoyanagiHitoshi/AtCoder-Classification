N=int(input())
A,B,C=[list(map(int,input().split())) for i in range(3)]
print(sum(B)+sum(C[A[i]-1] for i in range(N-1) if A[i]==(A[i+1]-1)))