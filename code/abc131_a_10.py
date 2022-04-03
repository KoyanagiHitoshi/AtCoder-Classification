S=input()
print("Bad" if any(S[i]==S[i+1] for i in range(len(S)-1)) else "Good")