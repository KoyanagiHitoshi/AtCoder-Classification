N,K=map(int,input().split())
A=list(map(int,input().split()))
city=0
if K<=N:
    for k in range(K):
        city=A[city]-1
    print(city+1)
else:
    visited=[-1]*N
    for k in range(K):
        if visited[city]!=-1:
            roop_start=visited[city]
            cycle_num=k-roop_start
            break
        visited[city]=k
        city=A[city]-1
    K=(K-roop_start)%cycle_num+roop_start
    city=0
    for k in range(K):
        city=A[city]-1
    print(city+1)