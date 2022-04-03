import numpy as np
K=int(input())
r=np.arange(1,K+1)
print(np.sum(np.gcd.outer(np.gcd.outer(r,r),r)))