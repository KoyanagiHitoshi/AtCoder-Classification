ABC = [int(input()) for i in range(3)]
sort = sorted(ABC)[::-1]
for i in ABC:
    print(sort.index(i)+1)