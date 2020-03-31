N=int(input())
A=[int(input()) for i in range(N)]
sort=sorted(A)
x,y=sort[-1],sort[-2]
for a in A:
    print(x if a!=x else y)