x = [[1, 6, 8], [3, 5, 7], [2, 4, 9]]
a, b, c = map(max, zip(*x))
print(a, b, c)
