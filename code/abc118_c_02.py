import functools
import math
N=int(input())
A=list(map(int,input().split()))
print(functools.reduce(math.gcd,A))