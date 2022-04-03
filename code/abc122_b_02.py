import re
S=input()
print(max(map(len,re.findall("[ACGT]*",S))))