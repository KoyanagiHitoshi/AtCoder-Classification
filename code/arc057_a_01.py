A,K=map(int,input().split())
t=A
ans=0
if K==0:
    ans=2*(10**12)-A
else:
    while t<2*(10**12):
        t=t+1+K*t
        ans+=1
print(ans)