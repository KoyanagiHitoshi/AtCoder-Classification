s=input()
ans=0
count=0 if s[0]=="B" else 1
for i in range(1,len(s)):
    if s[i]=="W":
        ans+=i-count
        count+=1
print(ans)