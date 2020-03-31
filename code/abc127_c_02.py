N,M=map(int,input().split())
L,R=0,N
for i in range(M):
    l,r=map(int,input().split())
    L,R=max(L,l),min(R,r)
print(max(R-L+1,0))