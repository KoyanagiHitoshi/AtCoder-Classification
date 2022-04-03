N=int(input())
move=10**12
for n in range(1,int(N**.5)+1):
    if N%n==0:
        move=min(move,N//n+n-2)
print(move)