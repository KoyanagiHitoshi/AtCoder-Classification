import itertools
import operator
x = [1, 2, 3, 4, 5]
for v in itertools.accumulate(x, func=operator.mul):
    print(v)
