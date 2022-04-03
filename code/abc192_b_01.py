S=input()
flag=True
for i in range(len(S)):
    if i%2==0 and not S[i].islower():
        flag=False
    if i%2==1 and not S[i].isupper():
        flag=False
print("Yes" if flag else "No")