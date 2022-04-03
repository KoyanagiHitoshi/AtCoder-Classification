S=input()
tile=S[::2].count("0")+S[1::2].count("1")
print(min(tile,len(S)-tile))