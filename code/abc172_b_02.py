S = input()
T = input()
count = 0
for s, t in zip(S, T):
    if s != t:
        count += 1
print(count)