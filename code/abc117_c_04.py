N,M=map(int,input().split())
X=sorted(map(int,input().split()))
diff=[0]*(M-1)
for i in range(M-1):
    diff[i]=X[i+1]-X[i]
print(sum(sorted(diff)[::-1][N-1:]))