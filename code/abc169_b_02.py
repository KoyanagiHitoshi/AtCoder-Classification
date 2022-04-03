N=int(input())
A=sorted(map(int,input().split()))
mul=1
for a in A:
    mul*=a
    if mul>10**18:
        mul=-1
        break
print(mul)