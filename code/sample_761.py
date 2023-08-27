import itertools
U = [1, 2]
V = [3, 4]
for u, v in itertools.product(U, V):
    print(u, v)
