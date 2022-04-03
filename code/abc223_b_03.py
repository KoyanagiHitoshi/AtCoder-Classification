S=input()
s=[S[i:]+S[:i] for i in range(len(S))]
print(min(s))
print(max(s))