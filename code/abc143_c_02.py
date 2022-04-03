import itertools
N=int(input())
S=input()
print(len(list(itertools.groupby(S))))