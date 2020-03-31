A,K=map(int,input().split())
t=A
ans=0
z=2*(10**12)
if K==0:ans=z-A
else:
    while t<z:
        t=t+1+K*t
        ans+=1
print(ans)