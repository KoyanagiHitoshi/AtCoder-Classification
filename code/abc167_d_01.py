N,K=map(int,input().split())
A=list(map(int,input().split()))
if K<=N:
    next_city=0
    for i in range(K):
        next_city=A[next_city]-1
else:
    next_city=0
    visited=[-1]*N
    visited[0]=0
    for num in range(1,N):
        next_city=A[next_city]-1
        if visited[next_city]!=-1:
            break
        visited[next_city]=num
    K=(K-num)%(num-visited[next_city])
    for i in range(K):
        next_city=A[next_city]-1
print(next_city+1)