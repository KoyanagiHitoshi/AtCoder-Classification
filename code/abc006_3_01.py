N,M=map(int,input().split())
if 2*N<=M<=4*N:
    y=M%2
    z=((M-3*y)-2*(N-y))//2
    x=N-y-z
    print(x,y,z)
else:
    print("-1 -1 -1")