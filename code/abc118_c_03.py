import functools
import fractions
N=int(input())
A=list(map(int,input().split()))
print(functools.reduce(fractions.gcd,A))