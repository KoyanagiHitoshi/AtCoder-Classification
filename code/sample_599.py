import itertools
x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(list((key, list(group)) for key, group in itertools.groupby(x)))
