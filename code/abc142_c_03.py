import numpy
N=int(input())
A=list(map(int,input().split()))
print(*numpy.argsort(A)+1)