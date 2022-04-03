X,K,D=map(int,input().split())
X=abs(X)
step=min(K,X//D)
print(abs(X-(step+(K-step)%2)*D))