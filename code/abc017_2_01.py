import re
print("NO" if re.sub(r"ch|o|k|u","",input()) else "YES")