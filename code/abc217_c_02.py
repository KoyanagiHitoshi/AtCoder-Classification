import numpy as np
N=int(input())
p=list(map(int,input().split()))
q=np.argsort(p)+1
print(*q)