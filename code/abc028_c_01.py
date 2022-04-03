from itertools import combinations
ABCDE=map(int,input().split())
print(sorted(map(sum,combinations(ABCDE,3)))[-3])