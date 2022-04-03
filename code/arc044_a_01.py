N=int(input())
flag=True
if N==1:
    flag=False
elif N==2 or N==3 or N==5:
    flag=True
elif N%2==0 or N%3==0 or N%5==0:
    flag=False
else:
    flag=True
print("Prime" if flag else "Not Prime")