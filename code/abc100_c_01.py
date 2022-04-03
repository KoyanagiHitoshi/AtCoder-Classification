N=int(input())
A=list(map(int,input().split()))
count=0
for a in A:
    while a%2==0:
        a,count=a/2,count+1
print(count)