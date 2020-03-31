s=input()[:-1]
while s[:len(s)//2]!=s[len(s)//2:]:s=s[:-1]
print(len(s))