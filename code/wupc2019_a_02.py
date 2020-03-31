s=input()[::-1]
for i in range(len(s)-1):
    if s[i:i+2]=="AW":s=s[:i]+"CA"+s[i+2:]
print(s[::-1])