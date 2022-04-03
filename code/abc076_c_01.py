import re
S=input().replace("?",".")
T=input()
for i in range(len(S)-len(T),-1,-1):
    if re.match(S[i:i+len(T)],T):
        S=S.replace(".","a")
        print(S[:i]+T+S[i+len(T):])
        break
else:
    print("UNRESTORABLE")