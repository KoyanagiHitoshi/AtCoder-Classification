N=int(input())
S=input()
if S[0]!=S[-1]:
    print(1)
else:
    for i in range(1,N-1):
        if S[0]!=S[i] and S[i+1]!=S[-1]:
            print(2)
            break
    else:
        print(-1)