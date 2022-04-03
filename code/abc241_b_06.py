from collections import Counter
N,M=map(int,input().split())
A=Counter(input().split())
B=Counter(input().split())
print("No" if B-A else "Yes")