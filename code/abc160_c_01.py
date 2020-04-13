K,N=map(int,input().split())
A=list(map(int,input().split()))
distance=max(A)-min(A)
for i in range(N):
    A.append(A[i]+K)
for i in range(N):
    distance=min(distance,A[i+N-1]-A[i])
print(distance)