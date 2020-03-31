S=input()
print("YES" if all(s==r or s=="*" or r=="*" for s,r in zip(S,S[::-1])) else "NO")