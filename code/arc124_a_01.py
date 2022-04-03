N,K=map(int,input().split())
C=[0]*(N+1)
count=0
for i in range(K):
    c,k=input().split()
    C[int(k)]=c
    if c=="R":
        count+=1
MOD=998244353
ans=1
for i in range(1,N+1):
    if C[i]:
        if C[i]=="L":
            count+=1
        else:
            count-=1
    else:
        ans*=count
        ans%=MOD
print(ans)