n,m=map(int,input().split())
l=[0]*m
for i in range(n):
    L=[int(i) for i in input().split()]
    del L[0]
    for i in range(len(L)):
        l[L[i]-1]+=1
ans=0
for i in range(m):
    if l[i]==n:ans+=1
print(ans)