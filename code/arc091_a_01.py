N,M=map(int,input().split())
print(1 if N==1 and M==1 else max(N,M)-2 if N==1 or M==1 else N*M-2*N-2*M+4)