import re
print(max(map(len,re.findall("[ACGT]*",input()))))