import re
print(max(map(len,re.split("[^ACGT]",input()))))