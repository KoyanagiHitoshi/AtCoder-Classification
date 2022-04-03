N=int(input())
A=list(map(int,input().split()))
mul=1
for a in sorted(A):
    mul*=a
    if mul>10**18:
        mul=-1
        break
print(mul)