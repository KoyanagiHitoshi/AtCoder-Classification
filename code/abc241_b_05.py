N,M=map(int,input().split())
A=input().split()
B=input().split()
print("Yes" if all(A.count(b)>=B.count(b) for b in B) else "No")