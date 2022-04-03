K,T=map(int,input().split())
a=list(map(int,input().split()))
print(max(max(a)-(K-max(a))-1,0))