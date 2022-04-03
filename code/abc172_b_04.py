S = input()
T = input()
print(sum(1 for s, t in zip(S, T) if s != t))