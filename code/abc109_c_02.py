from fractions import gcd
n,d=map(int,input().split())
x=sorted(list(map(int,input().split()))+[d])
r=x[1]-x[0]
print(min(gcd(x[i+1]-x[i],r) for i in range(n)))