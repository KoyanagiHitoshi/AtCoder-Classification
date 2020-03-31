A,B,K=map(int,input().split())
print([n for n in range(1,min(A,B)+1) if A%n==B%n==0][-K])