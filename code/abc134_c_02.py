N=int(input())
A=[int(input()) for i in range(N)]
y,x=sorted(A)[-2:]
for a in A:
    print(x if a!=x else y)