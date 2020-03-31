s=input()
t=[]
for i in s:
    if i=="B" and len(t)!=0:t.pop()
    if i=="0" or i=="1":t.append(i)
print(*t,sep="")