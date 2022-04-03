N,M=map(int,input().split())
H=list(map(int,input().split()))
top=[True]*N
for i in range(M):
    A,B=map(int,input().split())
    if H[A-1]<=H[B-1]:
        top[A-1]=False
    if H[A-1]>=H[B-1]:
        top[B-1]=False
print(sum(top))