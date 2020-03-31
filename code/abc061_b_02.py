n,m=map(int,input().split())
l=[]
for i in range(m):l+=list(map(int,input().split()))
for j in range(1,n+1):print(l.count(j))