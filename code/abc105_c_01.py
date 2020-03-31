n=int(input())
x=""
while n!=0:
    x=str(n%2)+x
    n=-(n//2)
print(0 if x=="" else x)