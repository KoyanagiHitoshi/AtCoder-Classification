N,A,B=map(int,input().split())
P,Q,R,S=map(int,input().split())
for i in range(P,Q+1):
    for j in range(R,S+1):
        print("#" if i+j==A+B or j-i==B-A else ".",end="")
    print()