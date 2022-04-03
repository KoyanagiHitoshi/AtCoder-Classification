N,M=map(int,input().split())
A=set()
B=set()
for i in range(M):
    a,b=map(int,input().split())
    if a==1:
        A.add(b)
    if b==N:
        B.add(a)
print("IMPOSSIBLE" if len(A&B)==0 else "POSSIBLE")