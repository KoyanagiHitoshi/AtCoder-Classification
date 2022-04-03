N=int(input())
A=[int(input()) for i in range(N)]
B={a:i for (i,a) in enumerate(sorted(set(A)))}
for a in A:
    print(B[a])