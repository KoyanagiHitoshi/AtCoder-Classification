N=int(input())
ans=N
for i in range(N+1):
    count=0
    t=i
    while t>0:
        count+=t%6
        t//=6
    t=N-i
    while t>0:
        count+=t%9
        t//=9
    ans=min(ans,count)
print(ans)