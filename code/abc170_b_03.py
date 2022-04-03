X,Y=map(int,input().split())
for num in range(X+1):
    if 2*num+4*(X-num)==Y:
        print("Yes")
        break
else:
    print("No")