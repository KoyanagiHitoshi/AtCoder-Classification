N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]
X=[(x,i) for i,x in enumerate([int(input()) for i in range(Q)])]
AX=sorted(A+X)[::-1]
ans=[0]*Q
count=0
for x,i in AX:
    if i<Q:
        ans[i]=count
    else:
        count+=1
print(*ans,sep="\n")