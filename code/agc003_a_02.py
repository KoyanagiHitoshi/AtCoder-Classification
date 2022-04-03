S="".join(sorted(set(input())))
print("Yes" if S=="ENSW" or S=="NS" or S=="EW" else "No")