N=int(input())
ans=N
for b in range(60):
    a,c=divmod(N,2**b)
    ans=min(ans,a+b+c)
print(ans)