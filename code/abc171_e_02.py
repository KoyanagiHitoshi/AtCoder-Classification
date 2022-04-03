N=int(input())
a=list(map(int,input().split()))
XOR=0
for i in range(N):
    XOR^=a[i]
for i in range(N):
    print(XOR^a[i])