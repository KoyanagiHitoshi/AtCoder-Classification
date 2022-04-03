import re
X=input()
print("NO" if re.sub(r"ch|o|k|u","",X) else "YES")