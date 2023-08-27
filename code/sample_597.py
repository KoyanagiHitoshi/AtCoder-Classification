import itertools
s = "abcd"
for x, y in itertools.combinations_with_replacement(s, 2):
    print(x, y)
