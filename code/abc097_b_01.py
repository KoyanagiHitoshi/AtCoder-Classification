X=int(input())
bp=1
for b in range(1,X):
    for p in range(2,X):
        if b**p<=X:
            bp=max(bp,b**p)
        else:
            break
print(bp)