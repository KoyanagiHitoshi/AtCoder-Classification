S=input()
print("AC" if S[0]=="A" and "C" in S[2:-1] and S[1:].replace("C","",1).islower() else "WA")