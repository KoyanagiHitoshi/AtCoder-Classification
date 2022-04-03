A,B=map(int,input().split())
for C in range(256):
    if A^C==B:
        print(C)
        break