import collections
N=int(input())
S=collections.Counter(input() for i in range(N))
maximum=max(S.values())
dictionary=sorted(key for key,value in S.items() if value==maximum)
for d in dictionary:
    print(d)