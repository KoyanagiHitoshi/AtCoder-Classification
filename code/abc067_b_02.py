N,K=map(int,input().split())
l=list(map(int,input().split()))
print(sum(sorted(l)[::-1][:K]))