a=int(input())
b=int(input())
print((((a//b)+1)*b-a) if a%b!=0 else 0)