matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
weight = [2, 0, 0]
print([sum(i*j for i, j in zip(row, weight)) for row in matrix])
