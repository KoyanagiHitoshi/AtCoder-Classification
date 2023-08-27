import collections
x = collections.Counter(["a", "b", "b", "c", "c", "c"])
y = collections.Counter(["a", "a", "b", "b", "c", "c"])
print(x-y)
