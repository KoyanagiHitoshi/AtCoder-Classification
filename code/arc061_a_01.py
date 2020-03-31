S=input()
ans=0
for i in range(2**(len(S)-1)):
    tmp=S[0]
    for j in range(len(S)-1):
        if i&(1<<j):tmp+="+"
        tmp+=S[j+1]
    ans+=eval(tmp)
print(ans)