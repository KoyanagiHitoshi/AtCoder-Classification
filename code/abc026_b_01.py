import math
N=int(input())
R=[int(input()) for i in range(N)]
R=[r**2 for r in sorted(R)[::-1]]
print((sum(R[::2])-sum(R[1::2]))*math.pi)