import re
s=input().split()
N=int(input())
t=[input() for i in range(N)]
for i in range(len(s)):
    for NG in t:
        if re.fullmatch(NG.strip().replace("*","."),s[i]):
            s[i]="*"*len(s[i])
print(*s)