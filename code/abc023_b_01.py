import re
N=int(input())
S=input()
print(N//2 if re.match(r"^((bcabca)*b|(cabcab)*cabca|(abcabc)*abc)$",S) else -1)