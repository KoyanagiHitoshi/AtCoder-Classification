A1,A2,A3=map(int,input().split())
x=2*A2-A1-A3
k=max(0,(1-x)//2)
print(x+3*k)