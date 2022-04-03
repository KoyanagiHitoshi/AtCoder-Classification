a,b=map(int,input().split())
if 0<a:
    print("Positive")
elif a<=0<=b:
    print("Zero")
else:
    print("Positive" if (b-a)%2 else "Negative")