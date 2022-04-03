N,M=map(int,input().split())
disk=[int(input()) for i in range(M)]
case=list(range(N+1))
for listen in disk:
    case[case.index(listen)],case[0]=case[0],listen
for cd in case[1:]:
    print(cd)