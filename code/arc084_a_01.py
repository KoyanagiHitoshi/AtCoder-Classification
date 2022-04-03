import bisect
N=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
C=sorted(list(map(int,input().split())))
print(sum(bisect.bisect_left(A,b)*(N-bisect.bisect_right(C,b)) for b in B))