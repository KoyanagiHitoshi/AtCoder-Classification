import re
S=input()
print("YES" if re.search("i.*c.*t",S.lower()) else "NO")