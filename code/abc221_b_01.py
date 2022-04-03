S=list(input())
T=list(input())
if S==T:
    print("Yes")
else:
    for i in range(len(S)-1):
        S[i],S[i+1]=S[i+1],S[i]
        if S==T:
            print("Yes")
            break
        S[i],S[i+1]=S[i+1],S[i]
    else:
        print("No")