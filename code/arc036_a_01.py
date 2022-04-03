N,K=map(int,input().split())
t=[int(input()) for i in range(N)]
for day in range(3,N):
    if sum(t[day-3:day])<K:
        print(day)
        break
else:
    print(-1)