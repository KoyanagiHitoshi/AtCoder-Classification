S=input()
user=set()
for s in S.split():
    for name in s.split("@")[1:]:
        if name:
            user.add(name)
for name in sorted(user):
    print(name)