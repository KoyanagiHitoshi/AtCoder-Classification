N=int(input())
S=""
while N>0:
    if N%2==0:
        S+="B"
        N//=2
    else:
        S+="A"
        N-=1
print(S[::-1])