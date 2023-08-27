keys = [1, 2, 3, 2, 1, 2]
x = [0]*3
for key in keys:
    x[key-1] += 1
print(*x)
