N,X=map(int,input().split())
m=[int(input()) for i in range(N)]
print(N+((X-sum(m))//min(m)))