import re
s=input().split()
N=int(input())
t=[input() for i in range(N)]
for i in range(len(s)):
    for NG in t:
        if len(s[i])==len(NG):
            s[i]=re.sub(NG.replace("*","."),"*"*len(s[i]),s[i])
print(*s)