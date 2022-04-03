import re
S=input()
print("YES" if re.search("[i|I].*[c|C].*[t|T]",S) else "NO")