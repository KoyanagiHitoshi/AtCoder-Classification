n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
l=[0]*n
for i in range(n):l[i]=max(v[i]-c[i],0)
print(sum(l))