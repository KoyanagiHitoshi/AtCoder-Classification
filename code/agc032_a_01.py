n=int(input())
b=list(map(int,input().split()))
a=[0]*(n+1)
a[0]=0
for i in b:a.insert(int(i)-1,i)
if sum(a[:n])==sum(b):
    for i in range(n):
        print(a[i])
else:print(-1)