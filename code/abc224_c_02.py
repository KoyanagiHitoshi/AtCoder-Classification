from itertools import combinations
N=int(input())
XY=[list(map(int,input().split())) for i in range(N)]
ans=0
for a,b,c in combinations(XY,3):
    if (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])!=0:
        ans+=1
print(ans)