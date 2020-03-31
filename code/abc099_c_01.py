N=int(input())
ans=N
for i in range(N+1):
    j=N-i
    cnt=0
    while i>0:
        cnt+=i%6
        i//=6
    while j>0:
        cnt+=j%9
        j//=9
    ans=min(ans,cnt)
print(ans)