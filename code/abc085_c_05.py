n,y=map(int,input().split())
y//=1000
a=y%5
for i in range(n+1):
    if a==i%5:
        b=(y-i)//5
        c=n-i
        if c<=b<=2*c:
            print(b-c,2*c-b,i)
            exit()
print(-1,-1,-1)