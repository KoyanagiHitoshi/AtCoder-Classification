n=int(input())
B=list(map(int,input().split()))
a=[0]
for b in B:a.insert(b-1,b)
if sum(a[:n])==sum(B):
    for i in range(n):print(a[i])
else:print(-1)