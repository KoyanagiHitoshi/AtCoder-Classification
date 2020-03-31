from collections import Counter
S=Counter(input())
T=Counter(input())
s=S.values()
t=T.values()
print("Yes" if sorted(s)==sorted(t) else "No")