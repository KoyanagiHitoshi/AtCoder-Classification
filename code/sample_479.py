x = ["b", "c", "a"]
y = sorted((alphabet, number) for number, alphabet in enumerate(x, 1))
for alphabet, number in y:
    print(alphabet, number)
