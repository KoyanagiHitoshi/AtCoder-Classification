S=input()
T=input()
diff=set()
for s,t in zip(S,T):
	diff.add((ord(s)-ord(t))%26)
print("Yes" if len(diff)==1 else "No")