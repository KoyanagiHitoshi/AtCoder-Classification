import functools
import math
x = [6, 12, 9]
print(functools.reduce(math.gcd, x))
