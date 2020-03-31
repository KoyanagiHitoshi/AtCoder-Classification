from collections import Counter
S=Counter(input())
print("Yes" if len(S)==2 and len(set(list(S.values())))==1 else "No")