from collections import Counter
N,K=map(int,input().split())
A=Counter(input().split())
print(sum(sorted(A.values(),reverse=True)[K:]))