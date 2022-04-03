N=int(input())
a=list(map(int,input().split()))
average=sum(a)/N
for i in range(N):
    a[i]=abs(a[i]-average)
print(a.index(min(a)))