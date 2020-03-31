N=int(input())
s=0
for i in range(N):
    a,b=map(int,input().split())
    s+=a*b
print(int(s*1.05))