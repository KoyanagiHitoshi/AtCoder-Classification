import itertools
s=input()
print("".join(key+str(len(list(group))) for key,group in itertools.groupby(list(s))))