import itertools
s=list(input())
print("".join(key+str(len(list(group))) for key,group in itertools.groupby(s)))