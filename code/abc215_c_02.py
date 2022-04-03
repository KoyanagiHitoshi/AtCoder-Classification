import itertools
S,K=input().split()
print("".join(sorted(set(itertools.permutations(S)))[int(K)-1]))