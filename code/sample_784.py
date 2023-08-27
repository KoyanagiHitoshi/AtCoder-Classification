grid = [input() for _ in range(3)]
print(*[col.count("#") for col in zip(*grid)])
