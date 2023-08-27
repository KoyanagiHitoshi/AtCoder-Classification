a, b = 12, 8
x, y = max(a, b), min(a, b)
while y != 0:
    x, y = y, x % y
print(x)
