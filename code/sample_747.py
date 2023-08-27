import itertools
x = ["a", "b", "c"]
print(list(itertools.combinations_with_replacement(x, 2)))
print(len(list(itertools.combinations_with_replacement(x, 2))))
