A,B,K=map(int,input().split())
a=[num for num in range(1,A+1) if A%num==0]
b=[num for num in range(1,B+1) if B%num==0]
print(sorted(set(a)&set(b))[::-1][K-1])