N, M = map(int, input().split())
A = sorted(map(int, input().split()))[::-1]
print("Yes" if A[M-1] >= sum(A)/(4*M) else "No")