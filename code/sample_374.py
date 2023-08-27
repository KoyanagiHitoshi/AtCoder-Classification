x = [[1, 0], [0, 0], [1, 1], [1, 0], [0, 1], [0, 0]]
print(list(map(list, set(map(tuple, x)))))
