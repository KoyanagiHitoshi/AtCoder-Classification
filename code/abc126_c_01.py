N,K=map(int,input().split())
probability=0
for dice in range(1,N+1):
    coin=1/N
    point=dice
    while(point<K):
        point*=2
        coin/=2
    probability+=coin
print(probability)