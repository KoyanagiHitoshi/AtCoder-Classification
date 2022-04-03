X=input()
N=int(input())
S=[input() for i in range(N)]
d=[]
for i in range(N):
    d.append([S[i],S[i].translate(str.maketrans(X,"abcdefghijklmnopqrstuvwxyz"))])
for s,_ in sorted(d,key=lambda d:d[1]):
    print(s)