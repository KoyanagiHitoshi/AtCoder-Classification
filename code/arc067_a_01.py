import math
N=int(input())
fractorial=math.factorial(N)
mod=10**9+7
ans,num=1,2
while num*num<=fractorial:
    count=1
    while fractorial%num==0:
        count+=1
        fractorial//=num
    ans*=count
    num+=1
if fractorial!=1:
    ans*=2
print(ans%mod)