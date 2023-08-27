import re
s = "AxBxABxBAxAAAxBBBxABAxBAB"
print(re.findall("[AB]*", s))
