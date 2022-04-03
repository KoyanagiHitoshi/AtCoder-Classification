N,K=map(int,input().split())
A=[0]+list(map(int,input().split()))
city=1
if K<=N:
    for k in range(K):
        city=A[city]
    print(city)
else:
    visited=[-1]*(N+1)
    for k in range(K):
        if visited[city]!=-1:
            roop_start=visited[city]
            cycle_num=k-roop_start
            break
        visited[city]=k
        city=A[city]
    K=(K-roop_start)%cycle_num+roop_start
    city=1
    for k in range(K):
        city=A[city]
    print(city)