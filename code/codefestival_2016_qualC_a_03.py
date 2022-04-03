import re
s=input()
print("Yes" if re.match(".*C.*F",s) else "No")