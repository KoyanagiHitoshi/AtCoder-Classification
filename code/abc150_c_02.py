import itertools
N=int(input())
P,Q=[tuple(map(int,input().split())) for i in range(2)]
dictionary=sorted(itertools.permutations(P,N))
print(abs(dictionary.index(P)-dictionary.index(Q)))