import itertools
s = "abcd"
for x, y in itertools.combinations(s, 2):
    print(x, y)
