import bisect
N,Q=map(int,input().split())
A=sorted(map(int,input().split()))
X=[int(input()) for i in range(Q)]
for x in X:
    print(N-bisect.bisect_left(A,x))