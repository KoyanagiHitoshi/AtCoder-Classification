S=list(input())
while len(S)!=0:
    S.pop()
    if S[:len(S)//2]==S[len(S)//2:]:
        print(len(S))
        exit()