N=int(input())
A=list(map(int,input().split()))
degree=[0,360]
point=0
for a in A:
    point=(point+a)%360
    degree.append(point)
degree.sort()
ans=0
for i in range(N+1):
    ans=max(ans,degree[i+1]-degree[i])
print(ans)