import itertools
S,K=input().split()
print("".join(sorted(set(itertools.permutations(S,len(S))))[int(K)-1]))