import math
import functools
def lcm(x: int, y: int) -> int: return x*y//math.gcd(x, y)
def lcmm(n: int) -> int: return functools.reduce(lcm, n)


x = [2, 3, 5]
print(lcmm(x))
