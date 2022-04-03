N,M,K=map(int,input().split())
flag=False
for n in range(N+1):
    for m in range(M+1):
        if (N-n)*m+(M-m)*n==K:
            flag=True
print("Yes" if flag else "No")