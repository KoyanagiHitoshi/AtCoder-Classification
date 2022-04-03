S=input()
N=len(S)
before=0
for i in range(N):
    if S[i]=="a":
        before+=1
    else:
        break
after=0
for i in range(N):
    if S[-1-i]=="a":
        after+=1
    else:
        break
S=S[before:N-after]
print("Yes" if S==S[::-1] and before<=after else "No")