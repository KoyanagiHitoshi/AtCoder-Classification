N,P=map(int,input().split())
A=list(map(int,input().split()))
print(sum(a<P for a in A))