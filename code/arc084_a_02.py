import bisect
N=int(input())
A=sorted(map(int,input().split()))
B=sorted(map(int,input().split()))
C=sorted(map(int,input().split()))
print(sum(bisect.bisect_left(A,b)*(N-bisect.bisect_right(C,b)) for b in B))