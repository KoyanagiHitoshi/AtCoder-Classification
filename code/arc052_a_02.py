import re
S=input()
print(*re.findall("[0-9]+",S))