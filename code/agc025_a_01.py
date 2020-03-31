N=int(input())
ans=10**5
for i in range(1,N):
    a=str(i)
    b=str(N-i)
    A=sum(map(int,a))
    B=sum(map(int,b))
    ans=min(ans,A+B)
print(ans)