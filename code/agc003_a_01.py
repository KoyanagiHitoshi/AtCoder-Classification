S=list(set(input()))
print("Yes" if len(S)==4 or (len(S)==2 and S.count("N")==S.count("S")) else "No")