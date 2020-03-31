n=int(input())
p=[[int(i)for i in input().split()] for _ in range(n)]
p.sort(key=lambda x: x[2])
a,b,c=p[-1]
for y in range(101):
    for x in range(101):
        h=c+abs(a-x)+abs(b-y)
        if all(k==max(h-abs(i-x)-abs(y-j),0) for i,j,k in p):
            print(x,y,h)
            exit()