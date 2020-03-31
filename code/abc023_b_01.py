import re
n=int(input())
f=re.match(r"^((bcabca)*b|(cabcab)*cabca|(abcabc)*abc)$",input())
print(n//2 if f else -1)