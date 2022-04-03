N,Q=map(int,input().split())
a=[0]*N
for i in range(Q):
    L,R,T=map(int,input().split())
    for i in range(L,R+1):
        a[i-1]=T
for i in range(N):
    print(a[i])