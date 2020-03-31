N=int(input())
H=list(map(int,input().split()))[::-1]
flag=True
base=H[0]
for i in range(N-1):
    if H[i]+1==H[i+1]:
        H[i+1]-=1
    elif H[i]>=H[i+1]:
        continue
    else:
        flag=False
print("Yes" if flag else "No")