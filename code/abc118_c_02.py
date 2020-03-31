import functools,fractions
n=int(input())
a=list(map(int,input().split()))
print(functools.reduce(fractions.gcd,a))