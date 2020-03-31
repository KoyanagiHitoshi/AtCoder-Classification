import math
n=int(input())
l=[int(input()) for i in range(5)]
print(math.ceil(n/min(l))+4)