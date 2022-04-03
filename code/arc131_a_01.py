A,B=[int(input()) for i in range(2)]
if B%2==0:
    print(str(A)+str(B//2))
else:
    print(str(A)+"0"+str(B*5))