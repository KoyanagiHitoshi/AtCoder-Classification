A,B,K=map(int,input().split())
print([num for num in range(1,min(A,B)+1) if A%num==B%num==0][-K])