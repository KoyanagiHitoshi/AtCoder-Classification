K=int(input())
ans=0
for a in range(1,2*10**5+1):
    for b in range(1,2*10**5+1):
        if a*b>K:
               break
        ans+=K//(a*b)
print(ans)