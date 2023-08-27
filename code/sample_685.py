import re
s = "test@example"
print(re.findall("@([a-z]+)", s))
