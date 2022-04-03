S=input()
N=len(S)
m,M=S,S
S+=S
for i in range(N):
    s=S[i:i+N]
    if s<m:
        m=s
    if s>M:
        M=s
print(m)
print(M)