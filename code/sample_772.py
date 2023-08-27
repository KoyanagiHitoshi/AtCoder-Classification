matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = list(map(list, zip(*matrix)))
print(transpose)
