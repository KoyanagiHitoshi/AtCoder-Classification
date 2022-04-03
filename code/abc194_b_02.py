N=int(input())
A,B=[],[]
for i in range(N):
    a,b=map(int,input().split())
    A+=[a]
    B+=[b]
print(min(max(A[i],B[j]) if i!=j else A[i]+B[j] for i in range(N) for j in range(N)))