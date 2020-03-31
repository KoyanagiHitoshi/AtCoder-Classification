N,A,B=map(int,input().split())
print(sum(i for i in range(N+1) if A<=sum(map(int,str(i)))<=B))