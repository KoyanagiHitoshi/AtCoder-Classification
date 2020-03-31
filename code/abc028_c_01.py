from itertools import combinations
S=map(int,input().split())
print(sorted(map(sum,combinations(S,3)))[-3])