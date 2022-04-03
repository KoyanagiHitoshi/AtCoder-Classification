import bisect
N=int(input())
A=[int(input()) for i in range(N)]
B=sorted(set(A))
for a in A:
    print(bisect.bisect_left(B,a))