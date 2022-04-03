import itertools
s=input()
string=""
for key,group in itertools.groupby(list(s)):
    string+=key+str(len(list(group)))
print(string)