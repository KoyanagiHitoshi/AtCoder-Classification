N=int(input())
A=list(map(int,input().split()))
if 0 in A:
    print(0)
else:
    mul=1
    for a in A:
        mul*=a
        if mul>10**18:
            print(-1)
            exit()
    print(mul)