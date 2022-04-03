from collections import Counter
n=int(input())
S=Counter(input())
for i in range(n-1):
    S&=Counter(input())
print("".join(sorted(S.elements())))