N=int(input())
d=list(map(int,input().split()))
print(sum(d[x]*d[y] for x in range(N) for y in range(x+1,N)))