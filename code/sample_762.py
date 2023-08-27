import itertools
U = [1, 2]
V = [3, 4]
print(sum(u*v for u, v in itertools.product(U, V)))
