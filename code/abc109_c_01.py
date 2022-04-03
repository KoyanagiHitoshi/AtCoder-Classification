from functools import reduce
import math
N,X=map(int,input().split())
x=[abs(X-int(i)) for i in input().split()]
print(reduce(math.gcd,x))