import collections
N=int(input())
S=collections.Counter([input() for i in range(N)])
print(S.most_common()[0][0])