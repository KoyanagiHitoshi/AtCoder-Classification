s=list(input())
a=[]
b=[]
for i in range(len(s)):
    if i%2==0:
        a.append("1")
        b.append("0")
    else:
        a.append("0")
        b.append("1")
a_count=0
b_count=0
for i in range(len(s)):
    if a[i]!=s[i]:a_count+=1
    if b[i]!=s[i]:b_count+=1
print(min(a_count,b_count))