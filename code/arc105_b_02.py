import math
import functools
N=int(input())
a=list(map(int,input().split()))
ans=functools.reduce(math.gcd,a)
print(ans)