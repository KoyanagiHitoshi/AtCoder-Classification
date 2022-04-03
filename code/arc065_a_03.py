import re
S = input()
print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")