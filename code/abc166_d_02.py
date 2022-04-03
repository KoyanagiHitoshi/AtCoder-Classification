X=int(input())
MAX=2*int(X**(1/5))+1
MIN=-2*int(X**(1/5))-1
for A in range(MIN,MAX):
    for B in range(MIN,MAX):
        if A**5-B**5==X:
            print(A,B)
            exit()