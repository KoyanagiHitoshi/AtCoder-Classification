N=int(input())
A=list(map(int,input().split()))
print(N*sum(a**2 for a in A)-sum(A)**2)