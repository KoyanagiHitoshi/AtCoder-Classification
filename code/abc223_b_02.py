S=input()
s=sorted(S[i:]+S[:i] for i in range(len(S)))
print(s[0])
print(s[-1])