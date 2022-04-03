from itertools import groupby
S=input()
K=int(input())
count=0
group=[len(list(value)) for key,value in groupby(S)]
for value in group:
    count+=value//2
count*=K
if S[0]==S[-1] and group[0]%2!=0 and group[-1]%2!=0:
    if len(S)==group[0]:
        count+=K//2
    else:
        count+=K-1
print(count)