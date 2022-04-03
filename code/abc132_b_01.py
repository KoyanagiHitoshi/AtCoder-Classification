n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(n-2):
    a,b,c=p[i],p[i+1],p[i+2]
    if a<=b<=c or c<=b<=a:
        count+=1
print(count)