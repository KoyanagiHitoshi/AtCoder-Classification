N=int(input())
name=""
while N>0:
    N-=1
    name+=chr(ord("a")+N%26)
    N//=26
print(name[::-1])