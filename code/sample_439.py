keys = ["a", "b", "c", "b", "a", "b"]
dictionary = {}
for key in keys:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
print(dictionary)
