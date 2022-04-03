S=list(input())
while len(S)!=0:
    S.pop()
    if len(S)%2==0 and S[:len(S)//2]==S[len(S)//2:]:
        print(len(S))
        break