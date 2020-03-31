import itertools
s=""
for i,j in itertools.groupby(list(input())):
    s+=i+str(len(list(j)))
print(s)