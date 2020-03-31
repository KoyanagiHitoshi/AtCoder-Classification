S=input()
M=0
count=0
for s in S:
    if s in "A":count+=1
    elif s in "C":count+=1
    elif s in "G":count+=1
    elif s in "T":count+=1
    else:
        count=0
    M=max(M,count)
print(M)