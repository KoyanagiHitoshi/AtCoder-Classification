S=input()
print("Bad" if any(S[i]==S[i+1] for i in range(3)) else "Good")