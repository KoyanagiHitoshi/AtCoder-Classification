t=[]
for x in input():
    if x=="B":
        try:t.pop()
        except:pass
    else:t.append(x)
print("".join(t))