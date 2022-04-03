X,K,D=map(int,input().split())
X=abs(X)
div,mod=divmod(X,D)
print(X-K*D if K<div else abs(mod-(K-div)%2*D))