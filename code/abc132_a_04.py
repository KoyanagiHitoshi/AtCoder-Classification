S=input()
s=list(set(S))
print("Yes" if len(s)==2 and S.count(s[0])==S.count(s[1])==2 else "No")