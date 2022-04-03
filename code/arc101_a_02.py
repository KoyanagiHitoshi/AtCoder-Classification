N,K=map(int,input().split())
x=sorted(map(int,input().split()))
print(min((min(abs(x[i])+abs(x[i+K-1]-x[i]),abs(x[i+K-1])+abs(x[i]-x[i+K-1]))) for i in range(N-K+1)))