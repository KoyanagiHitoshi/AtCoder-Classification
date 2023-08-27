x = [[0, 1], [1, 1], [1, 0], [0, 0]]
x.sort(key=lambda x: (x[0], -x[1]))
for i in x:
    print(i)
