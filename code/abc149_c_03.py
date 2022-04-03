X=int(input())
num=2
while num<X:
    if X%num==0:
        X+=1
        num=2
    else:
        num+=1
print(X)