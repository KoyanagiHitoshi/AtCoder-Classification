from bisect import bisect_right
N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=[0]*N
b=[0]*M
a[0]=A[0]
b[0]=B[0]
for i in range(N-1):
    a[i+1]=a[i]+A[i+1]
for i in range(M-1):
    b[i+1]=b[i]+B[i+1]
book=bisect_right(b,K)
for i in range(N):
    if a[i]>K:
        break
    j=bisect_right(b,K-a[i])
    book=max(book,(i+1)+j)
print(book)