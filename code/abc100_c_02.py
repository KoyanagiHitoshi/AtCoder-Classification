n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    while i%2==0:i,c=i/2,c+1
print(c)