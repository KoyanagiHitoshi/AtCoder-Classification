N=int(input())
xu=[input().split() for i in range(N)]
print(sum(float(x)*{"JPY":1,"BTC":380000}[u] for x,u in xu))