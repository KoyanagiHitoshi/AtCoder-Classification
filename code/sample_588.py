import itertools
x = [2, 1, 4, 3, 5]
for v in itertools.accumulate(x, func=max):
    print(v)
