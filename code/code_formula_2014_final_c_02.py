S=input()
user=[]
for s in S.split():
    for name in s.split("@")[1:]:
        if name:
            user.append(name)
for name in sorted(set(user)):
    print(name)