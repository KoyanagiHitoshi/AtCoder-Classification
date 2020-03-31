N,K=map(int,input().split())
T=[int(input()) for i in range(N)]
for i in range(3,N):
    if sum(T[i-3:i])<K:
        print(i)
        exit()
print(-1)