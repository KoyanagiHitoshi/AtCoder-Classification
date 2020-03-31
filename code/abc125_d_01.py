n=int(input())
A=list(map(int,input().split()))
B=[abs(a) for a in A]
count=0
ans=0
for i in range(n):ans+=abs(A[i])
if 0 in A:print(ans)
else:
    for i in range(n):
        if A[i]<0:count+=1
    if count%2==0:
        print(ans)
    else:
        print(ans-2*min(B))