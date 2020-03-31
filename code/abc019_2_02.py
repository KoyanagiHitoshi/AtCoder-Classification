import itertools
print("".join([i+str(len(list(j))) for i,j in itertools.groupby(list(input()))]))