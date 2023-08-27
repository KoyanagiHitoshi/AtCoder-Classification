a = [(x, y) for y in range(20) for x in range(10) if x+2*y == 5]
print(a)
a = list(map(list, set(a)))
print(a)
