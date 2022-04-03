N=int(input())
S=""
while N!=0:
    S=str(N%2)+S
    N=-(N//2)
print(0 if S=="" else S)