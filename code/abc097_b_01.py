x=int(input())
c=1
for b in range(1,x):
    for p in range(2,x):
        if b**p<=x:
            c=max(c,b**p)
        else:
            break
print(c)