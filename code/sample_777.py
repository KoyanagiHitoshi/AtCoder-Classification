matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([sum(row*2) for row in zip(*matrix)])
