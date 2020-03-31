N,M=map(int,input().split())
A=[input() for i in range(N)]
B=[input() for i in range(M)]
judge=any([line[j:j+M] for line in A[i:i+M]]==B for i in range(N-M+1) for j in range(N-M+1))
print("Yes" if judge else "No")