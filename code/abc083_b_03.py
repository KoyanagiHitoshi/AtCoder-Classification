N,A,B=map(int,input().split())
total=0
for num in range(N+1):
    if A<=sum(map(int,str(num)))<=B:
        total+=num
print(total)