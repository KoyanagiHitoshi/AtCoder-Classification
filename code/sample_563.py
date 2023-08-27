import collections
x = ["a", "a", "a", "a", "b", "c", "c"]
c = collections.Counter(x)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a

print(c.most_common()[0][1])
# 4

print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]

print(c.most_common(2))
# [('a', 4), ('c', 2)]

values, counts = zip(*c.most_common())
print(values)
# ('a', 'c', 'b')

print(counts)
# (4, 2, 1)

print(c["a"])
# 4

print(c["b"])
# 1

print(c["c"])
# 2

print(c["d"])
# 0
