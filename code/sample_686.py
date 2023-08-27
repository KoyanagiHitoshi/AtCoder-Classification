import re
x = ["AB", "BA", "ABA"]
for s in x:
    print(re.fullmatch("AB", s))
