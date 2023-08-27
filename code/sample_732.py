x = [5, 3, 3, 1, 6, 1]
mapping = {val: num for num, val in enumerate(sorted(set(x)))}
print(list(map(lambda v: mapping[v], x)))
print(mapping)
