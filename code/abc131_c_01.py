import math
A,B,C,D=map(int,input().split())
A-=1
lcm=C*D//math.gcd(C,D)
print(B-B//C-B//D+B//lcm-(A-A//C-A//D+A//lcm))