N,K=map(int,input().split())
a=[int(input()) for i in range(N)]
day=0
while K>0:
    K-=a[day]
    day+=1
print(day)