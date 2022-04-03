import math
N=int(input())
ABCDE=[int(input()) for i in range(5)]
print(math.ceil(N/min(ABCDE))+4)