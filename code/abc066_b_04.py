S=input()[:-1]
while S[:len(S)//2]!=S[len(S)//2:]:
    S=S[:-1]
print(len(S))