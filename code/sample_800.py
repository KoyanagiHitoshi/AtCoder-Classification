import functools
x = [1, 2, 3, 4, 5]
print(functools.reduce(lambda a, b: a+b, x))  # 15(=1+2+3+4+5)
print(functools.reduce(lambda a, b: a-b, x))  # -13(=1-2-3-4-5)
print(functools.reduce(lambda a, b: a*b, x))  # 120(=1*2*3*4*5)
