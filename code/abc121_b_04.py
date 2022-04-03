import numpy as np
N,M,C=map(int,input().split())
B=np.array(input().split(),dtype=np.int32)
A=np.array([input().split() for i in range(N)],dtype=np.int32)
count=sum((np.dot(A,B)+C)>0)
print(count)