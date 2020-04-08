N, M = map(int, input().split())
A = sorted(map(int, input().split()))
print("Yes" if A[-M] >= sum(A)/(4*M) else "No")