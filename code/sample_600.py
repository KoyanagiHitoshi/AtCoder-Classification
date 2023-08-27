import itertools
x = "aabbbcdd"
print(list((key, list(group)) for key, group in itertools.groupby(x)))
