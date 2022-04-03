S=input()
odd=S[::2]
even=S[1::2]
print("No" if "L" in odd or "R" in even else "Yes")