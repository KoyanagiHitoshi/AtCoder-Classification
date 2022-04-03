T=int(input())
for i in range(T):
    N=int(input())
    if N%4==0:
        print("Even")
    elif N%2==0:
        print("Same")
    else:
        print("Odd")