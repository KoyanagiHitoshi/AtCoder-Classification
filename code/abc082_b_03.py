s=input()
t=input()
print("Yes" if sorted(s)<sorted(t)[::-1] else "No")