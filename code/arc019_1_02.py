S=input()
b="ODIZSB"
a="001258"
for i in range(6):
    S=S.replace(b[i],a[i])
print(S)