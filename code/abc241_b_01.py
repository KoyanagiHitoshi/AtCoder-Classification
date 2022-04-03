from collections import Counter
N,M=map(int,input().split())
A=Counter(map(int,input().split()))
B=Counter(map(int,input().split()))
print("Yes" if all(A[k]>=v for k,v in B.items()) else "No")