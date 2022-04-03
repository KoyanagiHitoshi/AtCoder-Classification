A,B,K=map(int,input().split())
R=range(A,B+1)
for num in sorted(set(R[:K])|set(R[-K:])):
    print(num)