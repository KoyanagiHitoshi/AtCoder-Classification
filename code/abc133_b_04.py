N,D=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
count=0
for i in range(N):
    for j in range(i+1,N):
        count+=(sum((y-z)**2 for y,z in zip(X[i],X[j]))**.5).is_integer()
print(count)