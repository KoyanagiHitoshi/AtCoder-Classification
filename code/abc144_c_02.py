N=int(input())
move=int(N**.5)
while N%move!=0:
    move-=1
print(N//move+move-2)