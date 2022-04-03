import numpy as np
N,M,C=map(int,input().split())
B=np.array(input().split(),dtype=np.int32)
count=0
for i in range(N):
    A=np.array(input().split(),dtype=np.int32)
    if sum(A*B)+C>0:
        count+=1
print(count)