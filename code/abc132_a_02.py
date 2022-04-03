S=input()
set_s=list(set(S))
print("Yes" if len(set_s)==2 and S.count(set_s[0])==S.count(set_s[1])==2 else "No")