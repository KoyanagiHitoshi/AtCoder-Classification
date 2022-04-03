N=int(input())
A=[int(input()) for i in range(N)]
sorted_A=sorted(A)
x,y=sorted_A[-1],sorted_A[-2]
for a in A:
    print(x if a!=x else y)