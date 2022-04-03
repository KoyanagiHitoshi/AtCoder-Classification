X,Y=map(int,input().split())
flag=False
for i in range(X+1):
    if 2*i+4*(X-i)==Y:
        flag=True
print("Yes" if flag else "No")