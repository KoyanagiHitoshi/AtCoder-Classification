X=input()
if len(set(list(X)))==1:
    print("Weak")
else:
    for i in range(3):
        if int(X[i])%10!=(int(X[i+1])-1)%10:
            print("Strong")
            break
    else:
        print("Weak")