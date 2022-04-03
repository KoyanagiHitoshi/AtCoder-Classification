import re
S=input()
print(max(map(len,re.split("[^ACGT]",S))))