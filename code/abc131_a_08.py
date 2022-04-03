S=input()
print("Good" if all(S[i]!=S[i+1] for i in range(len(S)-1)) else "Bad")