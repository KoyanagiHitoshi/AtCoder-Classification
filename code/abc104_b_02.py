import re
S=input()
print("AC" if re.match("^A[a-z]+C[a-z]+$",S) else "WA")