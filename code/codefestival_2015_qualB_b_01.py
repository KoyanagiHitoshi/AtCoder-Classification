N,M=map(int,input().split())
A=list(map(int,input().split()))
count=[0]*(M+1)
for a in A:
    count[a]+=1
answer=count.index(max(count))
print(answer if count[answer]>N/2 else "?")