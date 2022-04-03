X,K,D=map(int,input().split())
X=abs(X)
div=X//D
if K<=div:
    print(X-K*D)
else:
    if (K-div)%2==0:
        print(X%D)
    else:
        print(abs(X%D-D))