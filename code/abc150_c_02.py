import itertools
N=int(input())
P,Q=[list(map(int,input().split())) for i in range(2)]
dictionary=sorted(itertools.permutations(P,N))
print(abs(dictionary.index(tuple(P))-dictionary.index(tuple(Q))))