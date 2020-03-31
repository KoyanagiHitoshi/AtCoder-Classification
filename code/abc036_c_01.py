N=int(input())
A=[int(input()) for i in range(N)]
B={j:i for (i,j) in enumerate(sorted(set(A)))}
for a in A:
    print(B[a])