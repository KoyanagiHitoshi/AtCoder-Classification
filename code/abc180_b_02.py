import numpy as np
N=int(input())
x=list(map(int,input().split()))
print(int(np.linalg.norm(x,ord=1)))
print(np.linalg.norm(x,ord=2))
print(int(np.linalg.norm(x,ord=np.inf)))