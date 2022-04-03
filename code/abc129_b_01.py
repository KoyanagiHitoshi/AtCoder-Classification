N=int(input())
W=list(map(int,input().split()))
print(min(abs(sum(W[:i+1])-sum(W[i+1:])) for i in range(N)))