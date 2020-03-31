from collections import Counter
input()
L=Counter(input().split())
R=Counter(input().split())
print(sum([min(value,L[key]) for key,value in R.items()]))