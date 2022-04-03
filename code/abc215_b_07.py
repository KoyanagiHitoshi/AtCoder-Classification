import math
N=int(input())
k=int(math.log2(N))
print(k if 2**k<=N else k-1)