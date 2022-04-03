N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
ans=2*10**5
for i in range(N):
    for j in range(N):
        if i!=j:
            ans=min(ans,max(A[i],B[j]))
        else:
            ans=min(ans,A[i]+B[j])
print(ans)