N,S,T=map(int,input().split())
W=day=0
for i in range(N):
    W+=int(input())
    day+=S<=W<=T
print(day)