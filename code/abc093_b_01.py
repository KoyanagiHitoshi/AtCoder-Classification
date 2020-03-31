a,b,k=map(int,input().split())
r=range(a,b+1)
for i in sorted(set(r[:k])|set(r[-k:])):print(i)