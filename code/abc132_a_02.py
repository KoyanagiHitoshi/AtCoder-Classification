S=input()
l=list(set(S))
print("Yes" if len(l)==2 and S.count(l[0])==S.count(l[1])==2 else "No")