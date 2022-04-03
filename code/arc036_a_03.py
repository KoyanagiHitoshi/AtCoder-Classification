N,K=map(int,input().split())
t=[int(input()) for i in range(N)]
sleep=[0]*(N-2)
for i in range(N-2):
    sleep[i]=sum(t[i:i+3])
day=N
for i in range(N-2):
    if sleep[i]<K:
        day=min(day,i+3)
print(-1 if day==N else day)