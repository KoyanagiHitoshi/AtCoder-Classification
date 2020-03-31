X=int(input())
while True:
    for x in range(2,X):
        if X%x==0:
            break
    else:
        print(X)
        break
    X+=1