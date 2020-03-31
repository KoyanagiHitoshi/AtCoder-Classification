S=input()
m=0
count=0
for s in S:
    if s in "A":count+=1
    elif s in "C":count+=1
    elif s in "G":count+=1
    elif s in "T":count+=1
    else:count=0
    m=max(m,count)
print(m)