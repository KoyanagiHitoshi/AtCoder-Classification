a=[100,100,200]
while len(a)<20:
    a.append(a[-1]+a[-2]+a[-3])
print(a[-1])