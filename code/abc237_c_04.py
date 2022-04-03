S=input()
N=len(S)
pre=N-len(S.lstrip("a"))
post=N-len(S.rstrip("a"))
S=S[pre:N-post]
print("Yes" if S==S[::-1] and pre<=post else "No")