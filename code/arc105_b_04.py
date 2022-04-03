def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

N=int(input())
A=list(map(int,input().split()))
res=0
for a in A:
    res=gcd(res,a)
print(res)