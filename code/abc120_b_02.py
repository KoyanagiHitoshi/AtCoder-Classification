A,B,K=map(int,input().split())
a=[n for n in range(1,A+1) if A%n==0]
b=[n for n in range(1,B+1) if B%n==0]
print(sorted(set(a)&set(b))[::-1][K-1])