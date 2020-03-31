import numpy
N=int(input())
A=list(map(int,input().split()))
print(*numpy.array(A).argsort()+1)