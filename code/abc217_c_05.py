import numpy as np
N=int(input())
P=list(map(int,input().split()))
Q=np.argsort(P)+1
print(*Q)