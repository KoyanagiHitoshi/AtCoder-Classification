N,K=map(int,input().split())
t=[int(input()) for i in range(N)]
flag=True
day=2
for i in range(3,N):
    if flag and sum(t[i-3:i])>=K:
       day=i
    else:
       flag=False
print(-1 if day+1==N else day+1)