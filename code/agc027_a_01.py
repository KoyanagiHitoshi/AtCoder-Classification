N,x=map(int,input().split())
a=sorted(map(int,input().split()))
count=0
for i in range(N-1):
    x=x-a[i]
    if x>=0:count+=1
if x==a[N-1]:count+=1
print(count)