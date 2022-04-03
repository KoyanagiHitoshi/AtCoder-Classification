N=int(input())
X=list(map(int,input().split()))
P=round(sum(X)/N)
print(sum((x-P)**2 for x in X))