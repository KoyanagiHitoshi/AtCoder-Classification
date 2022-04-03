import bisect
A,B,Q=map(int,input().split())
INF=10**18
S=[-INF]+[int(input()) for i in range(A)]+[INF]
T=[-INF]+[int(input()) for i in range(B)]+[INF]
for q in range(Q):
    x=int(input())
    a=bisect.bisect_right(S,x)
    b=bisect.bisect_right(T,x)
    distance=INF
    for s in [S[a-1],S[a]]:
        for t in [T[b-1],T[b]]:
            distance1=abs(s-x)+abs(s-t)
            distance2=abs(t-x)+abs(s-t)
            distance=min(distance,distance1,distance2)
    print(distance)