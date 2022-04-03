N,M=map(int,input().split())
ab=[]
for i in range(M):
    ab+=list(map(int,input().split()))
for i in range(1,N+1):
    print(ab.count(i))