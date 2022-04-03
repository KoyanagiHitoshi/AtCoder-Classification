N=int(input())
a=list(map(int,input().split()))
XOR=0
for i in range(N):
    XOR^=a[i]
print("Yes" if XOR==0 else "No")