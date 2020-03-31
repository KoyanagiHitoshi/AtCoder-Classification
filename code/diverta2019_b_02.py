r,g,b,n=map(int,input().split())
count=0
for x in range(n+1):
    for y in range(n-x+1):
        z=(n-r*x-g*y)//b
        if 0<=z<=3000:
            if r*x+g*y+z*b==n:count+=1
print(count)