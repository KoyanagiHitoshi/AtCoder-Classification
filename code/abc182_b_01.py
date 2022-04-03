N=int(input())
A=list(map(int,input().split()))
ans=GCD=0
for k in range(2,1001):
    count=sum(a%k==0 for a in A)
    if GCD<count:
        GCD=count
        ans=k
print(ans)