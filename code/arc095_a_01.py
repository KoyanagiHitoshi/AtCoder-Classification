N=int(input())
X=list(map(int,input().split()))
sort=sorted(X)
left=sort[(N//2)-1]
right=sort[N//2]
for x in X:
    print(left if left<x else right)