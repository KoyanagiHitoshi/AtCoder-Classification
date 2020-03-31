n,x=map(int,input().split())
l=[int(input()) for _ in range(n)]
print(n+((x-sum(l))//min(l)))