import re
S=input()
usernames=re.findall("@[a-z]+",S)
for username in sorted(set(usernames)):
    print(username[1:])