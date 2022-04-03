import numpy as np
from itertools import combinations
N,D=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
count=0
for y,z in combinations(X,2):
    count+=(sum(diff**2 for diff in np.array(y)-np.array(z))**.5).is_integer()
print(count)