N,T=map(int,input().split())
total=time=0
for i in range(N):
    A=int(input())
    if A>total:
        time+=A-total
    total=A+T
print(total-time)