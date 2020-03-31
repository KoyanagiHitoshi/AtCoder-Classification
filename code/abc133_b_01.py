N,D=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
count=0
for i in range(N):
    for j in range(i+1,N):
        distance=0
        for d in range(D):distance+=pow(abs(X[i][d]-X[j][d]),2)
        if distance==int(distance**.5)**2:count+=1
print(count)