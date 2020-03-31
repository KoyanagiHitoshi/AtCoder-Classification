s=input()
print("Yes" if all([s.count(i)%2==0 for i in set(s)]) else "No")