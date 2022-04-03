from collections import Counter
S=Counter(list(input()))
T=Counter(list(input()))
S,T=list(S.values()),list(T.values())
print("Yes" if sorted(S)==sorted(T) else "No")