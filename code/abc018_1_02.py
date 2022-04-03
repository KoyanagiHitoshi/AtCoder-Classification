ABC=[int(input()) for i in range(3)]
for abc in ABC:
    print(3-sorted(ABC).index(abc))