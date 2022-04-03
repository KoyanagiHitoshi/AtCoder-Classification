def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return int(x/gcd(x,y))*y
def mod_lcm(n,mod):
    ans=1
    for i in range(2,n+1):
        ans=lcm(ans,i)
    return ans+mod
N=int(input())
ans=mod_lcm(N,1)
print(ans)