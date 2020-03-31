X=int(input())
for x in range(X,2*X):
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            break
    else:
        print(x)
        break