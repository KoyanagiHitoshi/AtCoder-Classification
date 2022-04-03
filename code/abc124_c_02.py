S=input()
print(min(S[::2].count("0")+S[1::2].count("1"),S[::2].count("1")+S[1::2].count("0")))