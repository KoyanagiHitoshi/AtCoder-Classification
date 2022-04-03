N=int(input())
A=list(map(int,input().split()))
x=min(max(A[:2**(N-1)]),max(A[2**(N-1):]))
print(A.index(x)+1)