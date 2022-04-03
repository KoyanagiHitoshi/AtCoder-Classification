N=int(input())
A=sorted(map(int,input().split()))
B=sorted(map(int,input().split()))
C=sorted(map(int,input().split()))
i,j,k=0,0,0
ans=0
while i<N:
    while j<N and B[j]<=A[i]:
        j+=1
    if j==N:
        break
    while k<N and C[k]<=B[j]:
        k+=1
    if k==N:
        break
    assert A[i]<B[j]<C[k]
    ans+=1
    i,j,k=i+1,j+1,k+1
print(ans)