N=int(input())
v=[0]*N
for i in range(N-1):
    a,b=map(int,input().split())
    v[a-1]+=1
    v[b-1]+=1
print("Yes" if N-1 in v else "No")