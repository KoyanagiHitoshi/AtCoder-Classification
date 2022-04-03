N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=A=0
for i in range(N):
    A=max(A,a[i])
    ans=max(ans,A*b[i])
    print(ans)