w=input()
print("Yes" if all([w.count(i)%2==0 for i in set(w)]) else "No")