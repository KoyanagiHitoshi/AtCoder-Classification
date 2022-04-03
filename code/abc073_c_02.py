from collections import Counter
N=int(input())
A=Counter(int(input()) for i in range(N))
print(sum(count%2 for count in A.values()))