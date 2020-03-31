N,K=map(int,input().split())
t=[int(input()) for i in range(N)]
for i in range(3,N):
    if sum(t[i-3:i])<K:
        print(i)
        break
else:
    print(-1)