import numpy as np
N=int(input())
xy=np.array([list(map(int,input().split())) for i in range(N)])
print(sum(np.linalg.norm(i-j) for i in xy for j in xy)/N)