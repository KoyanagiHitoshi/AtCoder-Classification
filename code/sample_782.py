grid = [input() for _ in range(3)]
print("\n".join(map("".join, zip(*grid))))
