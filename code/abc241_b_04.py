from collections import Counter
N,M=map(int,input().split())
A=Counter(map(int,input().split()))
B=Counter(map(int,input().split()))
print("Yes" if A&B==B else "No")