s=input()
print("Yes" if all([int(s.count(i))%2==0 for i in list(set(s))]) else "No")