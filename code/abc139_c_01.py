N=int(input())
H=list(map(int,input().split()))
h=[0]*N
count=0
for i in range(1,N):
    if H[i-1]>=H[i]:
        count+=1
    else:
        count=0
    h[i]=count
print(max(h))