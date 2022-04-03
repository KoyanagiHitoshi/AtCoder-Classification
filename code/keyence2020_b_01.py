N=int(input())
XL=sorted([list(map(int,input().split())) for i in range(N)],key=sum)
count=0
left=-10**9
for X,L in XL:
    if left<=X-L:
        count+=1
        left=X+L
print(count)