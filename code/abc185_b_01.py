N,M,T=map(int,input().split())
flag=True
battery=N
C=0
for m in range(M):
    A,B=map(int,input().split())
    battery-=A-C
    if battery<=0:
        flag=False
    battery+=B-A
    if battery>N:
        battery=N
    C=B
battery-=T-B
print("Yes" if flag and battery>0 else "No")