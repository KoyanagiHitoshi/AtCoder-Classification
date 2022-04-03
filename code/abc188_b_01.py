N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print("Yes" if sum(a*b for a,b in zip(A,B))==0 else "No")