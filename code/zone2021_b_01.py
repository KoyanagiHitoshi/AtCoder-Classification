N,D,H=map(int,input().split())
high=0
for i in range(N):
    d,h=map(int,input().split())
    a=(H-h)/(D-d)
    b=H-a*D
    high=max(high,b)
print(high)