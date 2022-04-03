A,B,C=sorted(map(int,input().split()))
print(A*B if A%2==B%2==C%2==1 else 0)