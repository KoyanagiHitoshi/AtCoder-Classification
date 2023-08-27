x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(x)):
    x[i] += x[i-1]
print(x)
