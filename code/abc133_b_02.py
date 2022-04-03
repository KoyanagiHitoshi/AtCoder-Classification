import numpy as np
from itertools import combinations
N,D=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
print(sum((sum(diff**2 for diff in np.array(y)-np.array(z))**.5).is_integer() for y,z in combinations(X,2)))