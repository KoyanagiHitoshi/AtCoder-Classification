from collections import Counter
s=Counter(input())
t=Counter(input())
S=sorted(s.values())
T=sorted(t.values())
print("Yes" if S==T else "No")