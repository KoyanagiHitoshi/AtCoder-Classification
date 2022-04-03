N,A,B=map(int,input().split())
print(sum(num for num in range(N+1) if A<=sum(map(int,str(num)))<=B))