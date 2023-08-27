import functools
import operator
x = [1, 2, 3, 4, 5]
print(functools.reduce(operator.add, x))  # 15(=1+2+3+4+5)
print(functools.reduce(operator.sub, x))  # -13(=1-2-3-4-5)
print(functools.reduce(operator.mul, x))  # 120(=1*2*3*4*5)
