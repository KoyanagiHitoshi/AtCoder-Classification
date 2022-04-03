N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp_a=[True]+[False]*(N-1)
dp_b=[True]+[False]*(N-1)
for i in range(N-1):
    if dp_a[i]:
        dp_a[i+1]|=abs(A[i]-A[i+1])<=K
        dp_b[i+1]|=abs(A[i]-B[i+1])<=K
    if dp_b[i]:
        dp_a[i+1]|=abs(B[i]-A[i+1])<=K
        dp_b[i+1]|=abs(B[i]-B[i+1])<=K
print("Yes" if dp_a[-1] or dp_b[-1] else "No")