S=input()
print("Yes" if S[::2].islower() and (len(S)==1 or S[1::2].isupper()) else "No")