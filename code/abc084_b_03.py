A,B=map(int,input().split())
S=input()
if 1<=A<=5 and 1<=B<=5:
    if len(S)==A+B+1:
        if S[0:A].isdecimal() and S[A+1:len(S)].isdecimal() and S[A]=="-":
            print("Yes")
            exit()
print("No")