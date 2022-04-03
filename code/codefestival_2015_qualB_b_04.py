N,M=map(int,input().split())
A=list(map(int,input().split()))
counter=[0]*(M+1)
for a in A:
    counter[a]+=1
answer=counter.index(max(counter))
print(answer if counter[answer]>N/2 else "?")