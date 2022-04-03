N=int(input())
K=int(input())
X=list(map(int,input().split()))
print(sum(min(x,K-x)*2 for x in X))