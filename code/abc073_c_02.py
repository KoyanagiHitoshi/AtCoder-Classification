from collections import Counter
N=int(input())
A=Counter([int(input()) for i in range(N)])
print(sum(1 if count%2 else 0 for count in A.values()))