N,M=map(int,input().split())
A=sum(map(int,input().split()))
print(N-A if N-A>=0 else "-1")