N,M=map(int,input().split())
R=10**5
L=0
for i in range(M):
    l,r=map(int,input().split())
    L=max(L,l)
    R=min(R,r)
print(max(R-L+1,0))