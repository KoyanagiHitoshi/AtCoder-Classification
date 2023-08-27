import itertools
x = [1, 2, 3]
print(sorted(map(sum, itertools.combinations(x, 2))))
