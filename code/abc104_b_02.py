s=input()
print("AC" if "C" in s[2:-1] and "A" in s and s[1:].replace("C","",1).islower() else "WA")