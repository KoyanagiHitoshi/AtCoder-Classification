N,M=map(int,input().split())
sc=[list(map(int,input().split())) for m in range(M)]
for i in range(10**N):
    if len(str(i))==N and all(str(i)[s-1]==str(c) for s,c in sc):
        print(i)
        break
else:
    print(-1)