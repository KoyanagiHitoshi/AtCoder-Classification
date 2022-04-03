A,B,C,D=map(int,input().split())
print(["Balanced","Left","Right"][(A+B>C+D)-(A+B<C+D)])