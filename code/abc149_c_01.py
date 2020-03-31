X=int(input())
for x in range(X,2*X):
    flag=True
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            flag=False
            break
    if flag:
        print(x)
        exit()