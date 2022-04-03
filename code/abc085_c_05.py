N,Y=map(int,input().split())
Y//=1000
a=Y%5
for i in range(N+1):
    if a==i%5:
        b=(Y-i)//5
        c=N-i
        if c<=b<=2*c:
            print(b-c,2*c-b,i)
            break
else:
    print(-1,-1,-1)