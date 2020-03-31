N=int(input())
A=[int(input()) for i in range(N)]
a=sorted(A)
x,y=a[-1],a[-2]
for i in range(N):
    if A[i]!=x:
        print(x)
    else:
        print(y)