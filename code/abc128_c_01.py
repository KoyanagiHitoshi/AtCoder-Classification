N,M=map(int,input().split())
s=[list(map(int,input().split()))[1:] for m in range(M)]
p=list(map(int,input().split()))
count=0
for i in range(1<<N):
    for m in range(M):
        switch=0
        for j in range(N):
            if (i>>j)&1 and j+1 in s[m]:
                switch+=1
        if switch%2!=p[m]:
            break
    else:
        count+=1
print(count)