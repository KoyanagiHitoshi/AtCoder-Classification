S=input()
set_S=list(set(S))
print("Yes" if len(set_S)==2 and S.count(set_S[0])==S.count(set_S[1])==2 else "No")