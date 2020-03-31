from fractions import gcd
A,B,C,D=map(int,input().split())
A-=1
lcm=C*D//gcd(C,D)
print(B-B//C-B//D+B//lcm-(A-A//C-A//D+A//lcm))