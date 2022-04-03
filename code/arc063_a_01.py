from itertools import groupby
S=input()
group=groupby(S)
print(len(list(group))-1)