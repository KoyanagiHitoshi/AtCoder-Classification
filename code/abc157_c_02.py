N,M=map(int,input().split())
S,C=[],[]
for m in range(M):
    s,c=map(int,input().split())
    S.append(s)
    C.append(c)
for i in range(10**N):
    if len(str(i))==N and all(str(i)[s-1]==str(c) for s,c in zip(S,C)):
        print(i)
        break
else:
    print(-1)