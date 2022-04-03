N=int(input())%30
X=[1,2,3,4,5,6]
for i in range(N):
    X[i%5+1],X[i%5]=X[i%5],X[i%5+1]
print(*X,sep="")