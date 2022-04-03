w=input()
print("Yes" if all(w.count(char)%2==0 for char in set(w)) else "No")