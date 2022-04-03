S=input()
N=len(S)
pre=0
for i in range(N):
    if S[i]=="a":
        pre+=1
    else:
        break
post=0
for i in range(N-1,-1,-1):
    if S[i]=="a":
        post+=1
    else:
        break
S=S[pre:N-post]
print("Yes" if S==S[::-1] and pre<=post else "No")