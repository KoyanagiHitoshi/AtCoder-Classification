N,M=map(int,input().split())
X=sorted(set(map(int,input().split())))
coordinate=[]
for i in range(M-1):
    coordinate.append(X[i+1]-X[i])
coordinate=sorted(coordinate)[::-1]
print(sum(coordinate[N-1:]))