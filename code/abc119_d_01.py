import bisect
A,B,Q=map(int,input().split())
INF=10**18
S=[-INF]+[int(input()) for i in range(A)]+[INF]
T=[-INF]+[int(input()) for i in range(B)]+[INF]
for q in range(Q):
    x=int(input())
    s=bisect.bisect_right(S,x)
    t=bisect.bisect_right(T,x)
    d=INF
    for i in [S[s-1],S[s]]:
        for j in [T[t-1],T[t]]:
            ds=abs(i-x)+abs(i-j)
            dt=abs(j-x)+abs(i-j)
            d=min(d,ds,dt)
    print(d)