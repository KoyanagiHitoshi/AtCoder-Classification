ans=1
n=int(input())
for i in range(1,n+1):
    ans*=i
    ans=ans%(10**9+7)
print(ans)