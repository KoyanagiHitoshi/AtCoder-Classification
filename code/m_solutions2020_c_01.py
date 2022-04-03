N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N-K):
    print("Yes" if A[i+K]>A[i] else "No")