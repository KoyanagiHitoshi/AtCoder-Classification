grid = [input() for _ in range(3)]
print(*[row.count("#") for row in grid])
