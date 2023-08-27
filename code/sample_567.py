import collections
x = [("a", 1), ("b", 1), ("a", 2), ("c", 2)]
d = collections.defaultdict(list)
for key, value in x:
    d[key].append(value)
print(d)
