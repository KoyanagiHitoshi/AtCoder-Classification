import re
x = ["A", "C", "A1", "1A", "A1A", "1A1"]
for s in x:
    print(re.sub(r"\D", "*", s))
