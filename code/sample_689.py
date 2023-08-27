import re
x = ["atcoder", "ac", "ca", "ccaaccaa"]
for s in x:
    print(re.search("a.*c", s))
