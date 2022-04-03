import numpy as np
N=int(input())
a=list(map(int,input().split()))
print(np.gcd.reduce(a))