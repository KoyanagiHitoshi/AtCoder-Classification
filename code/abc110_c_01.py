S=input()
T=input()
print("Yes" if sorted(map(S.count,set(S)))==sorted(map(T.count,set(T))) else "No")