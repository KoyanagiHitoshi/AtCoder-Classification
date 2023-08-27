import itertools
x = "AAAABBBCCDAA"
print(list((key, len(list(group))) for key, group in itertools.groupby(x)))
