s=input()
t=input()
count=-1
for i in range(len(s)):
    if s==t:
        count=i
        break
    s=s[-1]+s[:-1]
print(count)