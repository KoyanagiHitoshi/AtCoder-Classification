import functools
import math
x = [15, 25, 30]
print(functools.reduce(math.gcd, x))
