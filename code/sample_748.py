import itertools
x = range(1, 4)
print(list(itertools.combinations_with_replacement(x, 2)))
print(len(list(itertools.combinations_with_replacement(x, 2))))
